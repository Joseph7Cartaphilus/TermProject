from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

from .models import Pin, PinCategory
from .forms import PinForm


class PinCategoryModelTestCase(TestCase):
    """Тест кейс для категорий пинов"""

    def setUp(self):
        self.category = PinCategory.objects.create(name="Test Category")

    def test_str_representation(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_unique_name_constraint(self):
        with self.assertRaises(Exception):
            PinCategory.objects.create(name="Test Category")


class PinModelTestCase(TestCase):
    """Тест кейс для пинов"""

    def setUp(self):
        self.category = PinCategory.objects.create(name="Test Category")
        self.user_data = {"username": "testuser", "password": "testpassword"}
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.image = SimpleUploadedFile(name="test_image.jpg", content=b"", content_type="image/jpeg")
        self.pin = Pin.objects.create(img=self.image, category=self.category, user=self.user)

    def test_str_representation(self):
        self.assertEqual(str(self.pin), "Pin %d" % self.pin.id)

    def test_image_upload(self):
        self.assertIsNotNone(self.pin.img)

    def test_foreign_key_constraint(self):
        with self.assertRaises(Exception):
            Pin.objects.create(img=self.image, category=None, user=self.user)


class AddPinViewTestCase(TestCase):
    """Тест кейс добавление пинов"""

    def setUp(self):
        self.client = Client()
        self.url = reverse("add_pin")
        self.user_data = {"username": "testuser", "password": "testpassword"}
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_login(self.user)

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], PinForm)
