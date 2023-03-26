from django import forms
from music.models import Track


class TrackForm(forms.ModelForm):
    """Форма создание трека"""

    class Meta:
        model = Track
        fields = ['title', 'artist', 'audio_file', 'img']
