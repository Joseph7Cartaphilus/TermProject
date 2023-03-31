from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from unittest.mock import patch

from music.models import Track, Artist, Playlist
from music.forms import TrackForm, PlaylistForm, AddTrackPlaylistForm


class TrackListViewTestCase(TestCase):
    """Тест кейс для списка треков"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('add_track')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_login(self.user)

        self.artist = Artist.objects.create(name='Test Artist')
        self.track1 = Track.objects.create(title='Test Track 1', artist=self.artist, user=self.user)
        self.track2 = Track.objects.create(title='Test Track 2', artist=self.artist, user=self.user)
        self.track3 = Track.objects.create(title='Test Track 3', artist=self.artist, user=self.user)

    def test_track_upload(self):
        self.assertIsNotNone(self.track1.title)


class TrackListAddViewTestCase(TestCase):
    """Тест кейс добавления треков"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('add_track')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_login(self.user)

    def test_track_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], TrackForm)


class PlaylistListViewTestCase(TestCase):
    """Тест кейс для списка плейлистов"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('add_playlist')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_login(self.user)

        self.playlist = Playlist.objects.create(title='Test Playlist', user=self.user)

    def test_playlist_upload(self):
        self.assertIsNotNone(self.playlist.title)


class PlaylistListAddViewTestCase(TestCase):
    """Тест кейс добавления плейлистов"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('add_playlist')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_login(self.user)

    def test_playlist_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PlaylistForm)


class Track_To_PlaylistListViewTestCase(TestCase):
    """Тест кейс для списка треков в  плейлистов"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('add_track_to_playlist')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_login(self.user)

        self.playlist = Playlist.objects.create(title='Test Playlist', user=self.user)

    def test_playlist_upload(self):
        self.assertIsNotNone(self.playlist.title)


class TrackPlaylistListAddViewTestCase(TestCase):
    """Тест кейс добавления трека в плейлист"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('add_track_to_playlist')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_login(self.user)

    def test_playlist_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AddTrackPlaylistForm)
