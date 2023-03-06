# Generated by Django 4.1.7 on 2023-03-06 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pins.pincategory', verbose_name='Pin Category'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='img',
            field=models.ImageField(upload_to='images/', verbose_name='Pin image'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='slug',
            field=models.SlugField(default='', verbose_name='Pin slug'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='text',
            field=models.TextField(blank=True, max_length=90, null=True, verbose_name='Pin description'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Pin name'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Pin user'),
        ),
        migrations.AlterField(
            model_name='pincategory',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Pin Category description'),
        ),
        migrations.AlterField(
            model_name='pincategory',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Pin Category name'),
        ),
    ]
