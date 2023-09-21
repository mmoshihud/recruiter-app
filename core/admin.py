from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User
from organization.models import Organization, OrganizationUser


class UserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active", "created_at")
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("name", "email", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                    "password1",
                    "password2",
                    "phone",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, UserAdmin)
admin.site.register(Organization)
admin.site.register(OrganizationUser)
