import requests
import discord
import os
from discord.ext import commands
from googleapiclient.discovery import build

# Gets the absolute path of call.py to fetch statistics
api_key = os.environ.get('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

class LinkVideo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Last Video 2 cog loaded')

    @commands.command()
    async def linklastvideo(self, ctx, userID):
        requestIMG = youtube.channels().list(
            part='snippet',
            id=f'{userID}'
        )
        requestId = youtube.activities().list(
            part='contentDetails',
            channelId=f'{userID}'
        )

        responseId = requestId.execute()
        responseIMG = requestIMG.execute()
        responseUsername = responseIMG['items'][0]['snippet']['title']
        responsePFP = responseIMG['items'][0]['snippet']['thumbnails']['medium']['url']
        videoId = responseId['items'][0]['contentDetails']['upload']['videoId']

        await ctx.channel.send(f'**{responseUsername}** Just Posted!\nhttps://youtu.be/{videoId}')

async def setup(bot):
    await bot.add_cog(LinkVideo(bot))