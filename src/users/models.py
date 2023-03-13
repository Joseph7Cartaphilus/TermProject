from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    """Модель пользователя"""
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Avatar')

    groups = models.ManyToManyField(
        Group,
        related_name='users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='users',
        blank=True,
        help_text='Specific permissions for this user.'
    )

