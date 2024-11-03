"""Main synchronization logic."""
import os
import time
from typing import Set
import logging
from config import Config
from spotify_client import SpotifyClient
from metadata_handler import MetadataHandler

logger = logging.getLogger(__name__)


class SyncManager:
    def __init__(self, spotify_client: SpotifyClient, metadata_handler: MetadataHandler):
        self.spotify_client = spotify_client
        self.metadata_handler = metadata_handler
        self.processed_tracks: Set[str] = set()

    def log_not_found(self, track_name: str, artist_name: str) -> None:
        """Log tracks not found on Spotify."""
        with open(Config.LOG_FILE, "a", encoding='utf-8') as file:
            file.write(f"Not found on Spotify: {track_name} by {artist_name}\n")

    def process_file(self, file_path: str, playlist_id: str) -> None:
        """Process a single audio file."""
        track_name, artist_name = self.metadata_handler.get_metadata(file_path)

        if not all([track_name, artist_name]):
            return

        track_id = self.spotify_client.search_track(track_name, artist_name)

        if not track_id:
            logger.info(f"Not found on Spotify: {track_name} by {artist_name}")
            self.log_not_found(track_name, artist_name)
            return

        if track_id in self.processed_tracks:
            return

        if self.spotify_client.is_track_in_playlist(track_id, playlist_id):
            logger.info(f"'{track_name}' by '{artist_name}' is already in the playlist.")
            return

        if self.spotify_client.is_track_liked(track_id):
            logger.info(f"'{track_name}' by '{artist_name}' is already liked.")
            return

        self.processed_tracks.add(track_id)

        playlist_success = self.spotify_client.add_track_to_playlist(track_id, playlist_id)
        like_success = self.spotify_client.like_track(track_id)

        if playlist_success and like_success:
            logger.info(f"Added '{track_name}' by '{artist_name}' to playlist and liked the track.")
        else:
            logger.error(f"Failed to add '{track_name}' by '{artist_name}' to playlist or like the track.")

        time.sleep(0.5)  # Rate limiting

    def sync_directory(self, music_dir: str, playlist_id: str) -> None:
        """Synchronize all supported audio files in directory with Spotify."""
        for root, _, files in os.walk(music_dir):
            for file in files:
                if file.lower().endswith(Config.SUPPORTED_FORMATS):
                    file_path = os.path.join(root, file)
                    self.process_file(file_path, playlist_id)