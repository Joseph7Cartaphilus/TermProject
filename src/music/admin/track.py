from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.utils.safestring import mark_safe

from music.models import Track


class TrackResource(resources.ModelResource):
    """Класс для импорта\экспорта треков"""

    class Meta:
        model = Track
        fields = ("title", "artist__name", "audio_file", "user__username")
        export_order = ("title", "artist__name", "audio_file", "user__username")


class TrackAdmin(ImportExportModelAdmin):
    """Отображение треков в админ панели"""

    fields = ["title", "audio_file", "img", "user", "artist"]
    list_display = ["title", "artist", "get_image"]
    ordering = ["-created_at"]
    list_per_page = 20
    resource_classes = [TrackResource]

    def get_image(self, obj):
        """Вывод изображений в административной панели"""
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="60" height="60">')
        else:
            return "-"

    get_image.short_description = "Track img"
