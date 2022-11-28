from googleapiclient.discovery import build
import os

api_key = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    id='UCNCYTj2rinrmtdRcp8NlbHw'
)

response = request.execute()