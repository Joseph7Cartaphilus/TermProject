from django.contrib import admin

from music.admin.track import TrackAdmin
from music.admin.artist import ArtistAdmin
from music.admin.playlist import PlaylistAdmin
from music.models import Track, Artist, Playlist

admin.site.register(Track, TrackAdmin)  # Регистрация модели Track в админке
admin.site.register(Artist, ArtistAdmin)  # Регистрация модели Artist в админке
admin.site.register(Playlist, PlaylistAdmin)  # Регистрация модели Playlist в админке
