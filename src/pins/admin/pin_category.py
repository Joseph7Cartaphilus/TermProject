from django.contrib import admin


class PinCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_per_page = 5
    ordering = ['name']