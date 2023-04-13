from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from .serializers import LoginSerializer, TokenResponseSerializer

from django.views.generic import CreateView
from .models import Contact
from .service import send
from .forms import ContactForm
from .tasks import send_spam_email, send_beat_email, send_password_reset_email


@swagger_auto_schema(
    method="POST", request_body=LoginSerializer, responses={status.HTTP_200_OK: TokenResponseSerializer()}
)
@api_view(["POST"])
@permission_classes([])
def auth_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(request, **serializer.validated_data)
    if user is None:
        raise AuthenticationFailed()
    token = Token.objects.create(user=user)
    response_data = {"token": token.key}
    response_serializer = TokenResponseSerializer(response_data)
    return Response(response_serializer.data)


def login_or_register(request: HttpRequest) -> HttpResponse:
    """Функция аутентификации и регистрации пользователя"""
    login_form = UserLoginForm(prefix="login")
    register_form = UserRegistrationForm(prefix="register")

    if "login-username" in request.POST:
        # Обработка формы аутентификации
        form = UserLoginForm(data=request.POST, prefix="login")
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("profile"))
    elif "register-email" in request.POST:
        # Обработка формы регистрации
        form = UserRegistrationForm(data=request.POST, prefix="register")
        if form.is_valid():
            user = form.save(commit=False)
            username = user.email.split("@")[0]
            user.username = username
            user.save()
            form.save()
            messages.success(request, "You have successfully registered")
            return HttpResponseRedirect(reverse("login_or_register"))
    return render(request, "forest.html", {"login_form": login_form, "register_form": register_form})


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    """Функция для авторизации пользователя профиль"""
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, "profile.html", {"form": form})


def main(request: HttpRequest) -> HttpResponse:
    """Основная страница parallax Forest"""
    return render(request, "main.html")


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = "contact.html"

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)  # работает
        send_spam_email.delay(form.instance.email)
        # send_beat_email.delay(form.instance.email)
        return super().form_valid(form)


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
    # generate reset password URL and pass it to the Celery task
        url = 'https://example.com/reset-password/'
        send_password_reset_email.delay(email, url)
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})
