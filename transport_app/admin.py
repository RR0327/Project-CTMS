from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Card, Schedule


class ScheduleAdmin(admin.ModelAdmin):
    """Admin configuration for Transport Schedules."""

    list_display = ("title", "date", "time", "updated_at")
    search_fields = ("title", "date")


class UserAdmin(BaseUserAdmin):
    """Admin configuration for the Custom User model."""

    list_display = ("email", "name", "role", "id_number", "level", "term", "is_admin")
    search_fields = ("email", "name", "role", "id_number", "level", "term")
    readonly_fields = ("id",)

    list_filter = ("is_admin", "role", "level", "term")

    # Organizing the detail view in Admin
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "name",
                    "role",
                    "id_number",
                    "level",
                    "term",
                    "contact_information",
                )
            },
        ),
        ("Permissions", {"fields": ("is_admin", "is_active")}),
    )

    # Required for adding new users via Admin panel
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "role",
                    "id_number",
                    "level",
                    "term",
                    "contact_information",
                    "password",
                ),
            },
        ),
    )

    ordering = ("email",)
    filter_horizontal = ()


# Registering models to the Admin site
admin.site.register(User, UserAdmin)
admin.site.register(Card)
admin.site.register(Schedule, ScheduleAdmin)
