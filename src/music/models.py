from django.db import models

from users.models import User


class BaseModel(models.Model):
    """Общая модель"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # Абстрактная модель
        abstract = True


class Artist(BaseModel):
    """Модель исполнителя"""
    name = models.CharField(max_length=255, verbose_name='Artist name')

    def __str__(self):
        """Представление объекта"""
        return self.name


class Track(BaseModel):
    """Модель трека"""
    title = models.CharField(max_length=255, verbose_name='Track title')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Track artist')
    img = models.ImageField(upload_to='cover/', null=False, blank=False, verbose_name='Music image')
    audio_file = models.FileField(upload_to='tracks/', null=False, blank=False, verbose_name='Track audio')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Track user')

    def __str__(self):
        """Представление объекта"""
        return self.title


class Playlist(BaseModel):
    """Модель плейлиста"""
    title = models.CharField(max_length=255, verbose_name='Playlist title')
    tracks = models.ManyToManyField(Track, verbose_name='Playlist tracks')
    img = models.ImageField(upload_to='posters/', null=False, blank=False, verbose_name='Playlist image')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Playlist user')

    def __str__(self):
        """Представление объекта"""
        return self.title
