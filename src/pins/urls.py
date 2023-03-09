from django.urls import path

from pins import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),  # Галерея пинов
    path('add_pin/', views.add_pin, name='add_pin'),  # Добавление пинов
    path('<int:category_id>/gallery/', views.gallery, name='category'),  # Категории пинов
]
