#!/usr/bin/env python3

"""Spotinoty script."""

import time
from subprocess import run  # noqa: S404

from spotinoty.spotify import Client


def say(song_info: str):
    """Run system say command.

    Args:
        song_info: string that represents current song info.
    """
    run(['/usr/bin/say', '-v', 'Alex', song_info], check=True)  # noqa: S603


def main():
    """Run the script.

    Raises:
        SystemExit: on KeyboardInterrupt
    """
    spotify = Client()
    prev_song = spotify.get_current_track()

    while True:
        current_song = spotify.get_current_track()
        if prev_song != current_song:
            say(current_song)
            prev_song = current_song
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            raise SystemExit('Exit.')


if __name__ == '__main__':
    main()
