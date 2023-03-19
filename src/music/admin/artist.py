from django.contrib import admin


class ArtistAdmin(admin.ModelAdmin):
    """Отображение исполнителей"""
    list_display = ['name']
    list_per_page = 5
    ordering = ['name']
