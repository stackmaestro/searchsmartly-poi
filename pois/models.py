from django.db import models
from django.core.serializers.json import DjangoJSONEncoder


class PointOfInterest(models.Model):
    name = models.CharField(max_length=255)
    external_id = models.CharField(max_length=255, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=255)
    ratings = models.JSONField(encoder=DjangoJSONEncoder, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def avg_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)
