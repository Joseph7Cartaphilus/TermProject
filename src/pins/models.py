from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from src.users.models import User


class BaseModel(models.Model):
    """General model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # Абстрактная модель
        abstract = True


class PinCategory(BaseModel):
    """Модель категория пинов"""
    name = models.CharField(max_length=64, unique=True, verbose_name='cat_name')
    description = models.TextField(null=True, blank=True, verbose_name='cat_desc')

    def __str__(self):
        """Представление объекта"""
        return self.name


class Pin(BaseModel):
    """Модель пина"""
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name='pin_name')
    text = models.TextField(max_length=90, null=True, blank=True, verbose_name='pin_desc')
    img = models.ImageField(upload_to='images/', null=False, blank=False, verbose_name='pin_img')
    slug = models.SlugField(default='', db_index=True, verbose_name='pin_slug')
    category = models.ForeignKey(PinCategory, on_delete=models.PROTECT, blank=True, null=True, verbose_name='pin_cat')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='pin_user')

    def __str__(self):
        """Представление объекта"""
        return f'Pin {self.id} - {self.title}'

    def save(self, *args, **kwargs):
        """Создание слага пина"""
        self.slug = slugify(self.title)
        super(Pin, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('pin_detail_slug_id', args=[self.slug, self.id])
