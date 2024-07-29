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


# This list of tracks should be replaced with the list of tracks from the spotify playlist
track_names = ["Me and the Birds", "The Perfect Girl", "Somebody That I Used to Know"]

# Get youtube videos from spotify track names
def get_video_id(track_name):
  request = youtube.search().list(
      part = 'snippet',
      q=track_name,
      type='video',
      maxResults=1
  )
  response = request.execute()
  return response['items'][0]['id']['videoId']

video_ids = []

# Find the first youtube video that shares its name with the spotify track
for track_name in track_names:
  video_id = get_video_id(track_name)
  video_ids.append(video_id)


