from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("login-or-register/", views.login_or_register, name="login_or_register"),  # Страница регистрации \ авторизации
    path("logout/", LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
    # Главная страница (Parallax Forest)
    path("profile/", views.profile, name="profile"),  # Страница профиля пользователя
    path("auth/", views.auth_view, name="auth"),  # Авторизация по токенам
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('password_reset/', views.password_reset, name='password_reset')
]
