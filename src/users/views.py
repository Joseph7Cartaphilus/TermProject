from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login_or_register(request: HttpRequest) -> HttpResponse:
    """Функция аутентификации и регистрации пользователя"""
    login_form = UserLoginForm(prefix='login')
    register_form = UserRegistrationForm(prefix='register')

    if 'login-username' in request.POST:
        # Обработка формы аутентификации
        form = UserLoginForm(data=request.POST, prefix='login')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('profile'))
    elif 'register-email' in request.POST:
        # Обработка формы регистрации
        form = UserRegistrationForm(data=request.POST, prefix='register')
        if form.is_valid():
            user = form.save(commit=False)
            username = user.email.split('@')[0]
            user.username = username
            user.save()
            form.save()
            messages.success(request, 'You have successfully registered')
            return HttpResponseRedirect(reverse('login_or_register'))
    return render(request, 'forest.html', {
        'login_form': login_form,
        'register_form': register_form
    })


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


def main(request: HttpRequest) -> HttpResponse:
    """Основная страница parallax Forest"""
    return render(request, 'main.html')
