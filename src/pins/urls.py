from django.urls import path

from pins import views

#  Пути для приложения 'pins'

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),  # Галерея пинов
    path('add_pin/', views.add_pin, name='add_pin'),  # Добавление пинов
    path('gallery/<int:category_id>', views.gallery, name='category'),  # Категории пинов
]
