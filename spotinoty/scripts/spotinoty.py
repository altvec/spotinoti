#!/usr/bin/env python3

"""Spotinoty script."""

import asyncio
import time

from spotinoty.spotify import get_token, get_track_info


async def say(song_info: str):
    """Run system say command.

    Args:
        song_info: string that represents current song info.
    """
    proc = await asyncio.create_subprocess_exec(
        '/usr/bin/say',
        '-v',
        'Alex',
        song_info,
        stdout=asyncio.subprocess.PIPE,
    )
    await proc.wait()


def main():
    """Run the script.

    Raises:
        SystemExit: If can't get access token from Spotify
    """
    token = get_token()
    if not token:
        raise SystemExit("Can't get access token!")

    prev_song = get_track_info(token)
    while True:
        try:
            current_song = get_track_info(token)
        except Exception:
            token = get_token()
        if prev_song != current_song:
            asyncio.run(say(current_song))
            prev_song = current_song
        time.sleep(10)


if __name__ == '__main__':
    main()
