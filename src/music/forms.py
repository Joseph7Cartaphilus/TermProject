from django import forms
from music.models import Track, Playlist


class TrackForm(forms.ModelForm):
    """Форма создание трека"""

    class Meta:
        model = Track
        fields = ["title", "artist", "audio_file", "img"]


class PlaylistForm(forms.ModelForm):
    """Форма создание плейлиста"""

    class Meta:
        model = Playlist
        fields = ["title", "img"]


class AddTrackPlaylistForm(forms.Form):
    tracks = forms.ModelMultipleChoiceField(queryset=Track.objects.all(), widget=forms.CheckboxSelectMultiple)
    playlist = forms.ModelChoiceField(queryset=Playlist.objects.all())
