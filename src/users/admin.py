from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.safestring import mark_safe

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Модель пользователя для Административной панели"""

    model = User
    readonly_fields = ("date_joined", "last_login", "is_active", "get_image")
    list_display_links = ("email", "username")
    list_display = ("email", "username", "get_image")
    fieldsets = (
        (
            "Info",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        (
            "Login",
            {
                "fields": ("date_joined", "last_login", "is_active"),
            },
        ),
        (
            "Staff",
            {
                "fields": ("is_superuser", "is_staff"),
            },
        ),
        (
            "User password",
            {
                "classes": ("collapse",),
                "fields": ("password",),
            },
        ),
        ("Image", {"fields": ("image", "get_image")}),
    )
    add_fieldsets = (
        (
            "Info",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                ),
            },
        ),
        ("Password", {"fields": ("password1", "password2")}),
        ("Image", {"fields": ("image",)}),
        ("Permissions", {"fields": ("is_superuser", "is_staff")}),
    )

    def get_image(self, obj):
        """Вывод изображений в административной панели"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="60">')
        else:
            return "-"

    get_image.short_description = "Avatar"
