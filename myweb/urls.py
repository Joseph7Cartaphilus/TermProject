from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),  # Главная страница (Parallax Forest)
    path('', include('social_django.urls', namespace='social')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
