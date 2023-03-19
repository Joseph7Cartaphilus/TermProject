from django.contrib import admin


class PlaylistAdmin(admin.ModelAdmin):
    """Отображение плейлистов"""
    list_display = ['title', 'user']
    fields = ['title', 'user', 'tracks']
    list_per_page = 10
    ordering = ['-created_at']
    filter_horizontal = ['tracks']