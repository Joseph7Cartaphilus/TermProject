from django.urls import path

from . import views

urlpatterns = [
    path("", views.player, name="player"),  # Плеер
    path("<int:artist_id>/", views.player, name="artist"),  # Фильтр по исполнителям
    path("playlists/", views.playlists, name="playlists"),  # Плейлисты
    path("playlist/<int:playlist_id>/", views.playlist, name="playlist"),  # Плейлист
    path("add_track/", views.add_track, name="add_track"),  # Добавление трека
    path("add_playlist/", views.add_playlist, name="add_playlist"),  # Добавление плейлиста
    path("add_track_to_playlist/", views.add_track_to_playlist, name="add_track_to_playlist"),
    # Добавление трека в плейлист
    path("playlist/<int:playlist_id>/delete/", views.playlist_delete, name="playlist_delete"),  # Удаление плейлиста
    path("playlist/<int:playlist_id>/edit/", views.playlist_edit, name="playlist_edit"),  # Редактирование плейлиста
]
