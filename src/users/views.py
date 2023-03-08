from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User
from django.views.generic import CreateView


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


def main(request):
    return render(request, 'main.html')


def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            send_password_reset_email.delay(user.email)
            messages.success(request, 'Password reset email has been sent')
        else:
            messages.error(request, 'User does not exist')
        return redirect('password_reset_request')
    return render(request, 'password_reset_request.html')


class ContactView(CreateView):  # TODO убрать
    success_url = "users/login.html"
    template_name = "users/password_reset_request"

    def form_valid(self, form):
        form.save()
        # send(form.instance.email) # работает
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)
