from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required

from music.models import Track, Artist


@login_required
def player(request: HttpRequest, artist_id=None) -> HttpResponse:
    """Функция для отображения всех треков | артистов"""
    context = {
        'tracks': Track.objects.all(),
        'artists': Artist.objects.all(),
    }
    if artist_id:
        context.update({'artists': Artist.objects.filter(id=artist_id)})
    else:
        context.update({'artists': Artist.objects.all()})
    return render(request, 'player.html', context)
