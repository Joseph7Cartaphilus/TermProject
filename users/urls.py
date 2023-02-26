from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('profile/', views.profile, name='profile')
]
