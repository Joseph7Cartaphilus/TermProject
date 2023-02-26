from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import UserLoginForm, UserRegistrationForm


class LoginTestCase(TestCase):
    """Тест кейс для функции login"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_login_success(self):
        response = self.client.post(self.url, data=self.user_data)
        self.assertRedirects(response, reverse('profile'))


class RegisterTestCase(TestCase):
    """Тест кейс для функции register"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('register')
        self.user_data = {
            'first_name': 'firstname',
            'last_name': 'last_name',
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password': 'testpassword',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_register_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertIsInstance(response.context['form'], UserRegistrationForm)


class LogoutTestCase(TestCase):
    """Тест кейс для функции logout"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.logout()

    def test_logout(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class ProfileTestCase(TestCase):
    """Тест кейс для функции profile"""
    def setUp(self):
        self.client = Client()
        self.url = reverse('profile')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.profile_url = reverse('profile')

    def test_profile_view_with_login(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
