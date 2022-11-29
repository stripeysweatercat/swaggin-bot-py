from googleapiclient.discovery import build
import os

userID = os.environ.get('PERIGON_ID')
austaID = os.environ.get('AUSTAMATE_ID')
rocketID = os.environ.get('ROCKET_ID')
fibesID = os.environ.get('FIBES_ID')
userName = 'schafer5'
api_key = os.environ.get('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

requestIMG = youtube.channels().list(
    part='snippet',
    id=f'{userID}'
)

requestStats = youtube.channels().list(
    part='statistics',
    id=f'{austaID}'
)

requestActivity = youtube.activities().list(
    part='snippet',
    channelId=f'{userID}'
)

requestVideo = youtube.videos().list(
    part='snippet',
    id='XZjR9xvd98Y'
)

responseIMG = requestIMG.execute()
responseActivity = requestActivity.execute()
responseVideo = requestVideo.execute()

responseUsername = responseIMG['items'][0]['snippet']['title']
responsePFP = responseIMG['items'][0]['snippet']['thumbnails']['medium']['url']

#videoId = responseActivity['items'][0]['contentDetails']['upload']['videoId']
videoTitle = responseActivity['items'][0]['snippet']['thumbnails']['maxres']['url']

print(responseVideo)