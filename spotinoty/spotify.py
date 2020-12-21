"""Spotify functions."""

import os

import spotipy
from dotenv import load_dotenv

load_dotenv()


def get_token() -> str:
    """Get acess token from Spotify.

    Returns:
        str
    """
    return spotipy.util.prompt_for_user_token(
        username=os.getenv('USERNAME'),
        scope=os.getenv('SCOPE'),
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    )


def get_track_info(token: str) -> str:
    """Get current track info.

    Args:
        token: access token

    Raises:
        SystemExit: if spotify app isn't running

    Returns:
        str
    """
    sp = spotipy.Spotify(auth=get_token())
    current_song = sp.currently_playing()
    if current_song is None:
        raise SystemExit("Spotify isn't playing.")

    artist = current_song['item']['artists'][0]['name']
    song_name = current_song['item']['name']
    return 'Now playing the {0} by {1}.'.format(song_name, artist)
