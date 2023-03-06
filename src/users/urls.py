from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views
from .views import ContactView # TODO убрать

urlpatterns = [
    path('login/', views.login, name='login'),  # Страница аутентификации
    path('register/', views.register, name='register'),  # Страница регистрации
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    # Главная страница (Parallax Forest)
    path('profile/', views.profile, name='profile'),  # Страница профиля пользователя
    path('password_reset/', views.password_reset_request, name='password_reset_request'),
    path("", ContactView.as_view(), name="contact")
]