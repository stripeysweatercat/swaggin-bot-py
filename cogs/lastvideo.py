import requests
import discord
import os
from discord.ext import commands
from googleapiclient.discovery import build

# Gets the absolute path of call.py to fetch statistics
api_key = os.environ.get('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

class LastVideo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Last Video cog loaded')

    @commands.command()
    async def lastvideo(self, ctx, userID):
        requestStats = youtube.channels().list(
            part='statistics',
            id=f'{userID}'
        )
        requestIMG = youtube.channels().list(
            part='snippet',
            id=f'{userID}'
        )
        requestId = youtube.activities().list(
            part='contentDetails',
            channelId=f'{userID}'
        )
        requestDetails = youtube.activities().list(
            part='snippet',
            channelId=f'{userID}'
        )

        responseDetails = requestDetails.execute()
        responseId = requestId.execute()
        responseStats = requestStats.execute()
        responseIMG = requestIMG.execute()
        responseUsername = responseIMG['items'][0]['snippet']['title']
        responsePFP = responseIMG['items'][0]['snippet']['thumbnails']['medium']['url']
        videoId = responseId['items'][0]['contentDetails']['upload']['videoId']
        videoImage = responseDetails['items'][0]['snippet']['thumbnails']['maxres']['url']
        videoTitle = responseDetails['items'][0]['snippet']['title']

        embed = discord.Embed(
            title=f'{videoTitle}',
            color=0x952828
            )
        embed.set_author(name=f'{responseUsername}\'s Latest Upload', url=f'https://youtu.be/{videoId}', icon_url=f'{responsePFP}')
        #embed.add_field(name=f'{videoTitle}', value='', inline=False)
        embed.set_image(url=f'{videoImage}')
        await ctx.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(LastVideo(bot))