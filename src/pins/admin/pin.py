from django.utils.safestring import mark_safe

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from src.pins.models import Pin


class PinResource(resources.ModelResource):
    class Meta:
        model = Pin
        fields = ('title', 'text', 'category__name', 'img', 'slug', 'user__username')
        export_order = ('title', 'text', 'category__name', 'img', 'slug', 'user__username')


class PinAdmin(ImportExportModelAdmin):
    fields = ['title', 'text', 'category', 'user', 'img', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'text', 'category', 'user', 'get_image', 'slug']
    ordering = ['title']
    list_per_page = 20
    resource_classes = [PinResource]

    def get_image(self, obj):
        """Вывод изображений в административной панели"""
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="50" height="60">')
        else:
            return '-'

    get_image.short_description = "Pin img"
