from googleapiclient.discovery import build
import os

userID = 'UCNCYTj2rinrmtdRcp8NlbHw'
austaID = 'UCX09eCnynW54idQDo1vEEqw'
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

responseIMG = requestIMG.execute()
responseActivity = requestActivity.execute()

responseUsername = responseIMG['items'][0]['snippet']['title']
responsePFP = responseIMG['items'][0]['snippet']['thumbnails']['medium']['url']

#videoId = responseActivity['items'][0]['contentDetails']['upload']['videoId']
videoTitle = responseActivity['items'][0]['snippet']['thumbnails']['maxres']['url']

print(videoTitle)