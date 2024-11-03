"""Spotify API client wrapper."""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException
from typing import Optional, Tuple
import logging

logger = logging.getLogger(__name__)


class SpotifyClient:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scope: str):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                scope=scope
            )
        )

    def search_track(self, track_name: str, artist_name: str) -> Optional[str]:
        """Search for a track on Spotify and return its ID."""
        if not track_name or not artist_name:
            return None

        query = f"track:{track_name} artist:{artist_name}"
        try:
            results = self.sp.search(q=query, type='track', limit=1)
            tracks = results['tracks']['items']
            return tracks[0]['id'] if tracks else None
        except SpotifyException as e:
            logger.error(f"Spotify search failed: {e}")
            return None

    def add_track_to_playlist(self, track_id: str, playlist_id: str) -> bool:
        """Add a track to the specified playlist."""
        try:
            self.sp.playlist_add_items(playlist_id, [track_id])
            return True
        except SpotifyException as e:
            logger.error(f"Failed to add track to playlist: {e}")
            return False

    def like_track(self, track_id: str) -> bool:
        """Add track to user's liked songs."""
        try:
            self.sp.current_user_saved_tracks_add([track_id])
            return True
        except SpotifyException as e:
            logger.error(f"Failed to like track: {e}")
            return False

    def is_track_in_playlist(self, track_id: str, playlist_id: str) -> bool:
        """Check if a track exists in the specified playlist."""
        try:
            results = self.sp.playlist_items(playlist_id)
            return any(track_id == item['track']['id'] for item in results['items'])
        except SpotifyException as e:
            logger.error(f"Failed to check track in playlist: {e}")
            return False

    def is_track_liked(self, track_id: str) -> bool:
        """Check if a track is in user's liked songs."""
        try:
            return self.sp.current_user_saved_tracks_contains([track_id])[0]
        except SpotifyException as e:
            logger.error(f"Failed to check if track is liked: {e}")
            return False