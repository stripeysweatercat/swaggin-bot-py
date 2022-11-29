import discord
import asyncio
import os
from googleapiclient.discovery import build

api_key = os.environ.get('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

testLoop = [1,2,3,4,5]

perigonID = os.environ.get('PERIGON_ID')
austaID = os.environ.get('AUSTAMATE_ID')
rocketID = os.environ.get('ROCKET_ID')
fibesID = os.environ.get('FIBES_ID')

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('loop bot online')

    async def my_background_task(self):
        await self.wait_until_ready()
        perigonPrevId = 'RTe2Icg7Vy8'
        perigonCurrentId = 0
        rocketPrevId = 'hd9Tu1qqVVU'
        rocketCurrentId = 0
        fibesPrevId = 'XZjR9xvd98Y'
        fibesCurrentId = 0
        austaPrevId = 'pjkIHN9WI9Y'
        austaCurrentId = 0
        channel = self.get_channel(1012280070557147196)
        while not self.is_closed():
            requestPerigon = youtube.activities().list(
                part='contentDetails',
                channelId=f'{perigonID}'
            )
            requestRocket = youtube.activities().list(
                part='contentDetails',
                channelId=f'{rocketID}'
            )
            requestFibes = youtube.activities().list(
                part='contentDetails',
                channelId=f'{fibesID}'
            )
            requestAustamate = youtube.activities().list(
                part='contentDetails',
                channelId=f'{austaID}'
            )
            responsePerigon = requestPerigon.execute()
            responseRocket = requestRocket.execute()
            responseFibes = requestFibes.execute()
            responseAusta = requestAustamate.execute()
            perigonVideoId = responsePerigon['items'][0]['contentDetails']['upload']['videoId']
            rocketVideoId = responseRocket['items'][0]['contentDetails']['upload']['videoId']
            fibesVideoId = responseFibes['items'][0]['contentDetails']['upload']['videoId']
            austaVideoId = responseAusta['items'][0]['contentDetails']['upload']['videoId']
            perigonCurrentId = perigonVideoId
            rocketCurrentId = rocketVideoId
            fibesCurrentId = fibesVideoId
            austaCurrentId = austaVideoId
            if perigonCurrentId != perigonPrevId:
                await channel.send(f'**Perigon** just posted!\nhttps://youtu.be/{perigonVideoId}')
                perigonPrevId = perigonCurrentId
            if rocketCurrentId != rocketPrevId:
                await channel.send(f'**Rocketsauce3** just posted!\nhttps://youtu.be/{rocketVideoId}')
                rocketPrevId = rocketCurrentId
            if fibesCurrentId != fibesPrevId:
                await channel.send(f'**Fibes** just posted!\nhttps://youtu.be/{fibesVideoId}')
                fibesPrevId = fibesCurrentId
            if austaCurrentId != austaPrevId:
                await channel.send(f'**Austamate** just posted!\nhttps://youtu.be/{austaVideoId}')
                austaPrevId = austaCurrentId
            await asyncio.sleep(60)
            


client = MyClient(intents=discord.Intents.default())
client.run(os.environ.get('DISCORD_TOKEN'))