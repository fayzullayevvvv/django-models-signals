from django.contrib import admin
from .models import Airport


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):

    # TABLE
    list_display = (
        "id",
        "name",
        "airport_code",
        "icao_code",
        "city",
        "country",
        "airport_type",
        "is_active",
        "is_24_hours",
        "created_at",
    )

    # CLICKABLE FIELD
    list_display_links = (
        "id",
        "name",
    )

    # FILTER RIGHT SIDE
    list_filter = (
        "airport_type",
        "country",
        "is_active",
        "is_24_hours",
        "supports_cargo",
        "supports_international_flights",
        "created_at",
    )

    # SEARCH
    search_fields = (
        "name",
        "airport_code",
        "icao_code",
        "city",
        "country",
        "city_code",
        "country_code",
    )

    # AUTO SLUG
    prepopulated_fields = {
        "slug": ("name",)
    }

    # DEFAULT SORT
    ordering = (
        "country",
        "city",
        "name",
    )

    # READONLY
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    # PAGINATION
    list_per_page = 20

    # SAVE BUTTON TOP
    save_on_top = True

    # FIELD GROUPS
    fieldsets = (

        ("Core Information", {
            "fields": (
                "name",
                "slug",
                "airport_code",
                "icao_code",
                "airport_type",
            )
        }),

        ("Location", {
            "fields": (
                "country",
                "country_code",
                "state",
                "state_code",
                "city",
                "city_code",
                "address",
                "zip_code",
                "latitude",
                "longitude",
                "timezone",
            )
        }),

        ("Airport Details", {
            "fields": (
                "terminals",
                "runways",
                "elevation_ft",
            )
        }),

        ("Contact", {
            "fields": (
                "website",
                "phone_number",
                "email",
            )
        }),

        ("Operational", {
            "fields": (
                "is_active",
                "is_24_hours",
                "supports_cargo",
                "supports_international_flights",
            )
        }),

        ("SEO / Metadata", {
            "fields": (
                "description",
            )
        }),

        ("Audit", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )