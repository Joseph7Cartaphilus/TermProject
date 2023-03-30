from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.utils.safestring import mark_safe

from pins.models import Pin


class PinResource(resources.ModelResource):
    """Класс для импорта\экспорта пинов"""
    class Meta:
        model = Pin
        fields = ('category__name', 'img', 'user__username')
        export_order = ('category__name', 'img', 'user__username')


class PinAdmin(ImportExportModelAdmin):
    """Отображение пинов в админ панели"""
    fields = ['img', 'category', 'user']
    list_display = ['get_image', 'category', 'user']
    ordering = ['-created_at']
    list_per_page = 20
    resource_classes = [PinResource]

    def get_image(self, obj):
        """Вывод изображений в административной панели"""
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="60" height="60">')
        else:
            return '-'

    get_image.short_description = "Pin img"
