# Generated by Django 4.1.7 on 2023-04-16 14:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movie_app", "0003_actor_description_en_actor_description_ru_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="actor",
            name="description_en",
        ),
        migrations.RemoveField(
            model_name="actor",
            name="description_ru",
        ),
        migrations.RemoveField(
            model_name="actor",
            name="name_en",
        ),
        migrations.RemoveField(
            model_name="actor",
            name="name_ru",
        ),
        migrations.RemoveField(
            model_name="category",
            name="description_en",
        ),
        migrations.RemoveField(
            model_name="category",
            name="description_ru",
        ),
        migrations.RemoveField(
            model_name="category",
            name="name_en",
        ),
        migrations.RemoveField(
            model_name="category",
            name="name_ru",
        ),
        migrations.RemoveField(
            model_name="genre",
            name="description_en",
        ),
        migrations.RemoveField(
            model_name="genre",
            name="description_ru",
        ),
        migrations.RemoveField(
            model_name="genre",
            name="name_en",
        ),
        migrations.RemoveField(
            model_name="genre",
            name="name_ru",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="country_en",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="country_ru",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="description_en",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="description_ru",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="tagline_en",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="tagline_ru",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="title_en",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="title_ru",
        ),
        migrations.RemoveField(
            model_name="movieshorts",
            name="description_en",
        ),
        migrations.RemoveField(
            model_name="movieshorts",
            name="description_ru",
        ),
        migrations.RemoveField(
            model_name="movieshorts",
            name="title_en",
        ),
        migrations.RemoveField(
            model_name="movieshorts",
            name="title_ru",
        ),
    ]
