from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),  # Главная страница (Parallax Forest)
    path('', include('social_django.urls', namespace='social')),  # OAuth 2
    path('users/', include('users.urls')),  # Приложение users
    path('pins/', include('pins.urls')),  # Приложение pins
    path('music/', include('music.urls')),  # Приложение music
    path('api/v1/', include('pins.urls')),  # api для приложения pins
]

# Настройка для MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
