from django.shortcuts import render

from music.models import Track


def player(request):
    context = {
        'tracks': Track.objects.all(),
    }
    return render(request, 'player.html', context)
