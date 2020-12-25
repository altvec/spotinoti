# Spotinoti

A silly command line tool that voices over the current track been playing on Spotify. Only works on macOS, because it uses built-in speech synthesis tool called `say`.

# Installation

```bash
pip install --user --extra-index-url https://test.pypi.org/simple/ spotinoti
```

Don't forget to populate `.env` file with your Spotify API credentials.


# Run as daemon

If you want to have this tool running as a daemon process, which starts automatically, you can use launchctl and the included plist. However, I do not recommend doing this because the script is very crude and Spotify API has rate limits. Pull-quests are welcome.

Anyway, to have it running as a deamon, fill the included `com.altvec.spotinoti.plist` with your Spotify API credentials, copy file into `~/Library/LaunchAgents/`, then execute:

```bash
launchctl load ~/Library/LaunchAgents/com.altvec.spotinoti.plist
```

This will load the script and immediately run the program.

To undo, use this:

```bash
launchctl unload ~/Library/LaunchAgents/com.altvec.spotinoti.plist
```

P.S After making changes in `com.altvec.spotinoti.plist`, don't forget to check it's correctness with `plutil`.