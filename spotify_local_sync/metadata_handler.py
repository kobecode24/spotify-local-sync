"""Audio file metadata handling."""
from tinytag import TinyTag
from typing import Tuple, Optional
import logging

logger = logging.getLogger(__name__)

class MetadataHandler:
    @staticmethod
    def clean_metadata(metadata: str) -> str:
        """Sanitize metadata to improve search results."""
        replacements = {
            ' (feat. ': ' ',
            ')': '',
            ' - Single Version': '',
            'by': '',
            '(': ''
        }
        for old, new in replacements.items():
            metadata = metadata.replace(old, new)
        return metadata.strip()

    @staticmethod
    def get_metadata(file_path: str) -> Tuple[Optional[str], Optional[str]]:
        """Extract metadata from an audio file."""
        try:
            tag = TinyTag.get(file_path)
            return (
                MetadataHandler.clean_metadata(tag.title),
                MetadataHandler.clean_metadata(tag.artist)
            )
        except Exception as e:
            logger.error(f"Error reading metadata from {file_path}: {e}")
            return None, None