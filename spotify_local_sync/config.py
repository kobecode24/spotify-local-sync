"""Configuration settings for the Spotify sync application."""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MUSIC_DIRECTORY = os.getenv('MUSIC_DIRECTORY')
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI', 'http://localhost:8888/callback')
    SPOTIFY_PLAYLIST_ID = os.getenv('SPOTIFY_PLAYLIST_ID')
    SPOTIFY_SCOPE = 'playlist-modify-public playlist-modify-private user-library-modify user-library-read'
    SUPPORTED_FORMATS = ('.mp3', '.wav', '.flac', '.aac', '.m4a', '.ogg')
    LOG_FILE = 'not_found_songs.log'