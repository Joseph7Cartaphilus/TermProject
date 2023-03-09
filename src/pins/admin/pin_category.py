from django.contrib import admin


class PinCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 5
    ordering = ['name']
