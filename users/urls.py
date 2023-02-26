from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # Страница аутентификации
    path('register/', views.register, name='register'),  # Страница регистрации
    path('logout/', views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    # Страница аутентификации (выход из системы)
    path('profile/', views.profile, name='profile')  # Страница профиля пользователя
]
