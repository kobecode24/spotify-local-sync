"""Entry point for the Spotify sync application."""
import logging
from config import Config
from spotify_client import SpotifyClient
from metadata_handler import MetadataHandler
from sync_manager import SyncManager


def setup_logging():
    """Configure logging settings."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('spotify_sync.log'),
            logging.StreamHandler()
        ]
    )


def main():
    """Main application entry point."""
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        spotify_client = SpotifyClient(
            client_id=Config.SPOTIFY_CLIENT_ID,
            client_secret=Config.SPOTIFY_CLIENT_SECRET,
            redirect_uri=Config.SPOTIFY_REDIRECT_URI,
            scope=Config.SPOTIFY_SCOPE
        )

        metadata_handler = MetadataHandler()
        sync_manager = SyncManager(spotify_client, metadata_handler)

        sync_manager.sync_directory(Config.MUSIC_DIRECTORY, Config.SPOTIFY_PLAYLIST_ID)

    except Exception as e:
        logger.error(f"Application error: {e}", exc_info=True)


if __name__ == "__main__":
    main()