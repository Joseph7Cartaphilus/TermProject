from django.utils.safestring import mark_safe

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from pins.models import Pin


class PinResource(resources.ModelResource):
    class Meta:
        model = Pin
        fields = ('category__name', 'img', 'user__username')
        export_order = ('category__name', 'img', 'user__username')


class PinAdmin(ImportExportModelAdmin):
    fields = ['category', 'user', 'img']
    list_display = ['category', 'user', 'get_image']
    ordering = ['-created_at']
    list_per_page = 20
    resource_classes = [PinResource]

    def get_image(self, obj):
        """Вывод изображений в административной панели"""
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="50" height="60">')
        else:
            return '-'

    get_image.short_description = "Pin img"
