from django.urls import path

from pins import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
]
