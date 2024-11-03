# Spotify Local Sync

Spotify Local Sync is a Python application that synchronizes your local music library with Spotify. It automatically adds your local music to a specified Spotify playlist and likes the tracks.

## Features

- Scans local music directory for audio files
- Extracts metadata from audio files
- Searches for tracks on Spotify
- Adds tracks to a specified playlist
- Likes tracks on Spotify
- Handles rate limiting
- Logs unmatched tracks
- Supports multiple audio formats (MP3, WAV, FLAC, AAC, M4A, OGG)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kobecode24/spotify-local-sync.git
   cd spotify-local-sync
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Spotify credentials:
   ```env
   MUSIC_DIRECTORY=your_music_directory_path
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
   SPOTIFY_PLAYLIST_ID=your_playlist_id
   ```

## Usage

Run the application:
```bash
python -m spotify_local_sync.main
```

## Configuration

- Create a Spotify Developer account at [Spotify Developer](https://developer.spotify.com/)
- Create a new application to get your client ID and client secret
- Set the redirect URI in your Spotify application settings
- Create a playlist on Spotify and get its ID from the share link

