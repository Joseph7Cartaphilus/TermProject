from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required

from music.models import Track, Artist, Playlist
from music.forms import TrackForm, PlaylistForm, AddTrackPlaylistForm


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


@login_required
def playlists(request: HttpRequest) -> HttpResponse:
    """Функция для отображения всех плейлистов"""
    context = {
        'playlists': Playlist.objects.all()
    }
    return render(request, 'playlists.html', context)


@login_required
def playlist(request: HttpRequest, playlist_id) -> HttpResponse:
    """Функция для отображения одного плейлиста"""
    track_lists = get_object_or_404(Playlist, id=playlist_id)
    tracks = track_lists.tracks.all()
    return render(request, 'playlist.html', {
        'track_lists': track_lists,
        'tracks': tracks
    })


@login_required
def add_track(request: HttpRequest) -> HttpResponse:
    """Функция создания трека"""
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            track = form.save(commit=False)
            track.user = request.user
            track.save()
            return redirect('player')
    else:
        form = TrackForm()
    return render(request, 'add_track.html', {'form': form})


@login_required
def add_playlist(request: HttpRequest) -> HttpResponse:
    """Функция создания плейлиста"""
    if request.method == 'POST':
        form = PlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            list = form.save(commit=False)
            list.user = request.user
            list.save()
            return redirect('playlists')
    else:
        form = PlaylistForm()
    return render(request, 'add_playlist.html', {'form': form})


@login_required
def add_track_to_playlist(request: HttpRequest) -> HttpResponse:
    """Функция добавление трека в плейлист"""
    if request.method == 'POST':
        form = AddTrackPlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.cleaned_data['playlist']
            tracks = form.cleaned_data['tracks']
            playlist.tracks.add(*form.cleaned_data['tracks'])
            return redirect('playlist', playlist_id=playlist.id)
    else:
        form = AddTrackPlaylistForm()

    return render(request, 'add_track_to_playlist.html', {
        'form': form,
    })

@login_required
def playlist_delete(request, playlist_id):
    """Функция для удаления плейлиста"""
    playlist = get_object_or_404(Playlist, id=playlist_id)
    if request.method == 'POST':
        playlist.delete()
        return redirect('playlists')
    return render(request, 'playlist_delete.html', {
        'playlist': playlist
    })
