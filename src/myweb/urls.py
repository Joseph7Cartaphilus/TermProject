from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from users import views
from myweb.yasg import urlpatterns as doc_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main, name="main"),  # Главная страница (Parallax Forest)
    path("", include("social_django.urls", namespace="social")),  # OAuth 2
    path("users/", include("users.urls")),  # Приложение users
    path("pins/", include("pins.urls")),  # Приложение pins
    path("music/", include("music.urls")),  # Приложение music
    path("movies/", include("movie_app.urls")),  # Приложение movie
    path("api/v1/", include("pins.urls")),  # api для приложения pins
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

urlpatterns += doc_urls  # Документация swagger

# Настройка для MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
