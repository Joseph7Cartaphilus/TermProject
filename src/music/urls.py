from django.urls import path

from . import views

urlpatterns = [
    path('', views.player, name='player'),
    path('<int:artist_id>/music/', views.player, name='artist'),
]
