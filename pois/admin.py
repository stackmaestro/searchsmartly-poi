from django.contrib import admin
from .models import PointOfInterest


@admin.register(PointOfInterest)
class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "external_id", "category", "display_avg_rating")
    search_fields = ("id", "external_id")
    list_filter = ("category",)

    def display_avg_rating(self, obj):
        return obj.avg_rating

    display_avg_rating.short_description = "Avg. Rating"

    readonly_fields = (
        "created_at",
        "updated_at",
    )
