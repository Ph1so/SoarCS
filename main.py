import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build

load_dotenv()

spotify_client_id = os.getenv('SPOTIFU_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

yt_api_key = "AIzaSyDP9zn4N1N0eg2OZWrKYVHbLAqofjPtrnU"
youtube = build("youtube", "v3", developerKey=yt_api_key)

