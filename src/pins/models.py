from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from users.models import User


class BaseModel(models.Model):
    """General model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # Абстрактная модель
        abstract = True


class PinCategory(BaseModel):
    """Модель категория пинов"""
    name = models.CharField(max_length=64, unique=True, verbose_name='Pin Category name')

    def __str__(self):
        """Представление объекта"""
        return self.name


class Pin(BaseModel):
    """Модель пина"""
    img = models.ImageField(upload_to='images/', null=False, blank=False, verbose_name='Pin image')
    category = models.ForeignKey(PinCategory, on_delete=models.PROTECT, null=False, blank=False, verbose_name='Pin Category')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Pin user')

    def __str__(self):
        """Представление объекта"""
        return f'Pin {self.id}'
