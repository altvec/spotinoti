"""Spotify functions."""

import os
from pathlib import Path

import spotipy
from dotenv import load_dotenv

load_dotenv()


class Client(object):
    """Spotify client."""

    def __init__(self):
        """Initialize client."""
        self.client = spotipy.Spotify(
            auth_manager=spotipy.SpotifyOAuth(
                scope=os.getenv('SCOPE'),
                cache_path=Path('/tmp') / '.cache-spotinoti',  # noqa: S108
            ),
        )

    def get_current_track(self) -> str:
        """Get current track info.

        Returns:
            str
        """
        current_song = self.client.currently_playing()
        artist = current_song['item']['artists'][0]['name']
        song_name = current_song['item']['name']
        return 'Now playing the {0} by {1}.'.format(song_name, artist)
