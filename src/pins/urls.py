from rest_framework import routers
from django.urls import path, include

from pins import views

#  Пути для приложения 'pins'

router = routers.DefaultRouter()
router.register(r"pins", views.PinViewSet)
router.register(r"categories", views.PinCategoryViewSet)

urlpatterns = [
    path("gallery/", views.gallery, name="gallery"),  # Галерея пинов
    path("add_pin/", views.add_pin, name="add_pin"),  # Добавление пинов
    path("gallery/<int:category_id>", views.gallery, name="category"),  # Категории пинов
    path("", include(router.urls)),
]
