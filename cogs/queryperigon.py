import youtube_api.ytapi.call as call
import requests
import discord
import os
from discord.ext import commands

# Gets the absolute path of call.py to fetch statistics
absolute_path = os.path.dirname(__file__)
relative_path = 'youtube_api\\ytapi\\call.py'
full_path = os.path.join(absolute_path, relative_path)
os.startfile(full_path)
response = call.response

class QueryPerigon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('QueryPerigon cog loaded')

    @commands.command()
    async def queryperigon(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blue,
            title='Perigon Statistics',
            url='https://www.youtube.com/channel/UCNCYTj2rinrmtdRcp8NlbHw',
            )
        embed.add_field(name='Subscribers', value=response['items'][0]['statistics']['subscriberCount'], inline=False)
        embed.add_field(name='Total Views', value=response['items'][0]['statistics']['viewCount'], inline=False)
        embed.add_field(name='Total Videos', value=response['items'][0]['statistics']['videoCount'], inline=False)
        await ctx.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(QueryPerigon(bot))