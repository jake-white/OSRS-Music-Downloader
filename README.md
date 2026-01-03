# OSRS-Music-Downloader
A simple python script that downloads OSRS music tracks from [the wiki](https://oldschool.runescape.wiki/w/Category:Music_tracks) and adds appropriate metadata. I was unable to find an up-to-date repository of these online, so here you go. Credit to [hirmuolio](https://www.reddit.com/r/2007scape/comments/z196e7/is_there_a_way_to_download_the_osrs_music_from/ixa8mt7/) for the idea and script that got me started.

## Usage
Requires at least Python 3.7 as well as `pymediawiki`, `yt_dlp`, and `taglib`.

To install dependencies:
```
pip install pymediawiki yt_dlp pytaglib
```

To run: `python3 osrsmusic.py` will autogenerate a "tracks" subfolder and fill it with ogg files. These will have the title, artist, and album details.

## Is this legal?
This script simply pulls from the files already being publicly hosted on the Wiki, so [I think so](https://x.com/RuneScape/status/1270839410469339137?lang=en).
