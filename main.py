import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build

load_dotenv()

spotify_client_id = os.getenv('SPOTIFU_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

yt_api_key = os.getenv('YT_API_KEY')
youtube = build("youtube", "v3", developerKey=yt_api_key)

