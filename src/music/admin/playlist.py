from django.contrib import admin
from django.utils.safestring import mark_safe


class PlaylistAdmin(admin.ModelAdmin):
    """Отображение плейлистов"""

    list_display = ["title", "user", "get_image"]
    fields = ["title", "user", "tracks", "img"]
    list_per_page = 10
    ordering = ["-created_at"]
    filter_horizontal = ["tracks"]

    def get_image(self, obj):
        """Вывод изображений в административной панели"""
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="60" height="60">')
        else:
            return "-"

    get_image.short_description = "Track img"
