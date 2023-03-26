from django.urls import path

from . import views

urlpatterns = [
    path('', views.player, name='player'),
    path('<int:artist_id>/', views.player, name='artist'),
    path('playlists/', views.playlists, name='playlists'),
    path('playlist/<int:playlist_id>/', views.playlist, name='playlist'),
]
