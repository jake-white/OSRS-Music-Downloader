from mediawiki import MediaWiki
import yt_dlp
import json
import taglib
import re

wiki = MediaWiki(url='https://oldschool.runescape.wiki/api.php')
wiki.user_agent = 'osrs-music-downloader'

track_names = wiki.categorymembers("Music_tracks", results=3000, subcategories=False )

print(f"Found {len(track_names)} tracks to download...")

# download the tracks
for track_name in track_names:
    track_name_formatted = track_name.replace("(music track)", "").strip() # removes disambiguation suffix
    
    # remove characters like ? from filenames which cause errors
    illegal_chars = r"[<>:\"/\\|?*]"
    track_name_formatted = re.sub(illegal_chars, "", track_name_formatted)
    
    ydl_opts = {"playlist_items":"1", # this *should* download the latest version only
            "outtmpl": f"tracks/{track_name_formatted}.ogg"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download( 'https://oldschool.runescape.wiki/w/' + track_name )
        
        # splitting sidebar wikitext to find composer
        page = wiki.page(track_name, auto_suggest=False)
        wikitext = page.wikitext.split("|")
        composer = "Unknown"
        for item in wikitext:
            match = re.match(r'composer\s*=\s*(.+)', item)
            if(match):
                composer = match.group(1)
        
        # loading file to add metadata
        filename = f"tracks/{track_name_formatted}.ogg"
        with taglib.File(filename, save_on_exit=True) as song:
            song.tags["ALBUM"] = "Old School Runescape OST"
            song.tags["ARTIST"] = composer
            song.tags["TITLE"] = track_name_formatted