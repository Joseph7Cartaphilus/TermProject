from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required

from music.models import Track, Artist


@login_required
def player(request: HttpRequest, artist_id=None) -> HttpResponse:
    """Функция для отображения всех треков | артистов"""
    query = request.GET.get('q')
    if query:
        tracks = Track.objects.filter(Q(title__icontains=query) | Q(artist__name__icontains=query))
    else:
        tracks = Track.objects.all()
    context = {
        'tracks': tracks,
        'artists': Artist.objects.all(),
        'query': query,
    }
    if artist_id:
        context.update({'artists': Artist.objects.filter(id=artist_id)})
    else:
        context.update({'artists': Artist.objects.all()})
    return render(request, 'player.html', context)


def playlists(request: HttpRequest) -> HttpResponse:
    """Функция для отображения всех плейлистов"""
    return render(request, 'playlists.html')