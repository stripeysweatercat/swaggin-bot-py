import requests
import discord
import os
from discord.ext import commands
from googleapiclient.discovery import build

# Gets the absolute path of call.py to fetch statistics
api_key = os.environ.get('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

class QueryStatistics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Query Statistics cog loaded')

    @commands.command()
    async def querystats(self, ctx, userID):
        requestStats = youtube.channels().list(
            part='statistics',
            id=f'{userID}'
        )
        requestIMG = youtube.channels().list(
            part='snippet',
            id=f'{userID}'
        )

        responseStats = requestStats.execute()
        responseIMG = requestIMG.execute()
        responseUsername = responseIMG['items'][0]['snippet']['title']
        responsePFP = responseIMG['items'][0]['snippet']['thumbnails']['medium']['url']

        embed = discord.Embed(
            title=f'{responseUsername} Statistics',
            url='https://www.youtube.com/channel/UCNCYTj2rinrmtdRcp8NlbHw',
            )
        embed.set_thumbnail(url=f'{responsePFP}')
        embed.add_field(name='Subscribers', value=responseStats['items'][0]['statistics']['subscriberCount'], inline=False)
        embed.add_field(name='Total Views', value=responseStats['items'][0]['statistics']['viewCount'], inline=False)
        embed.add_field(name='Total Videos', value=responseStats['items'][0]['statistics']['videoCount'], inline=False)
        await ctx.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(QueryStatistics(bot))