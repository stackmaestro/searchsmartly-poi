import csv
import json
import os
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand, CommandError
from pois.models import PointOfInterest
from django.db import transaction
from tqdm import tqdm


class Command(BaseCommand):
    help = "Import Points of Interest from CSV, JSON, and XML files"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options["file_path"]
        if not os.path.exists(file_path):
            raise CommandError(f"File '{file_path}' does not exist.")

        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() == ".csv":
            self.import_from_csv(file_path)
        elif file_extension.lower() == ".json":
            self.import_from_json(file_path)
        elif file_extension.lower() == ".xml":
            self.import_from_xml(file_path)
        else:
            self.stdout.write(
                self.style.ERROR(f"Unsupported file type: '{file_extension}'")
            )

    def import_from_csv(self, filename):
        try:
            batch_pois = []
            batch_size = 1000

            with open(filename, mode="r") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in tqdm(reader, desc="Importing CSV"):
                    ratings = self.parse_ratings(row["poi_ratings"])
                    poi = PointOfInterest(
                        external_id=row["poi_id"],
                        name=row["poi_name"],
                        latitude=float(row["poi_latitude"]),
                        longitude=float(row["poi_longitude"]),
                        category=row["poi_category"],
                        ratings=ratings,
                    )
                    batch_pois.append(poi)
                    if len(batch_pois) >= batch_size:
                        with transaction.atomic():
                            PointOfInterest.objects.bulk_create(
                                batch_pois, ignore_conflicts=True
                            )
                            batch_pois = []
                if batch_pois:
                    with transaction.atomic():
                        PointOfInterest.objects.bulk_create(
                            batch_pois, ignore_conflicts=True
                        )
        except Exception as e:
            raise CommandError(f"Error importing CSV file: {e}")

    def import_from_json(self, filename):
        try:
            with open(filename, mode="r") as json_file:
                data = json.load(json_file)
                for entry in tqdm(data, desc="Importing JSON"):
                    ratings = entry["ratings"]
                    PointOfInterest.objects.update_or_create(
                        external_id=entry["id"],
                        defaults={
                            "name": entry["name"],
                            "latitude": entry["coordinates"]["latitude"],
                            "longitude": entry["coordinates"]["longitude"],
                            "category": entry["category"],
                            "ratings": ratings,
                            "description": entry.get("description", ""),
                        },
                    )
        except Exception as e:
            raise CommandError(f"Error importing JSON file: {e}")

    def import_from_xml(self, filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            for elem in tqdm(root.findall("DATA_RECORD"), desc="Importing XML"):
                ratings = self.parse_ratings(elem.find("pratings").text.strip())
                PointOfInterest.objects.update_or_create(
                    external_id=elem.find("pid").text.strip(),
                    defaults={
                        "name": elem.find("pname").text.strip(),
                        "latitude": float(elem.find("platitude").text.strip()),
                        "longitude": float(elem.find("plongitude").text.strip()),
                        "category": elem.find("pcategory").text.strip(),
                        "ratings": ratings,
                    },
                )
        except Exception as e:
            raise CommandError(f"Error importing XML file: {e}")

    def parse_ratings(self, ratings_str):
        cleaned_ratings_str = ratings_str.strip("{}")
        return [float(rating) for rating in cleaned_ratings_str.split(",")]
