from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request: HttpRequest) -> HttpResponse:
    """Функция для аутентификации пользователя"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {
        'form': form
    })


def register(request: HttpRequest) -> HttpResponse:
    """Функция для регистрации пользователя"""
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {
        'form': form
    })


def logout(request: HttpRequest) -> HttpResponse:
    """Функция для выхода из системы"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('/'))


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    """Функция для авторизации пользователя профиль"""
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html', {
        'form': form
    })
