import discord
import asyncio
import os

from itertools import cycle
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)
status = cycle(['Status 1', 'Status 2', 'Status 3'])

@client.event
async def on_ready():
    change_status.start()
    print(f'{client.user} is online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)

    await message.channel.send
    
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await client.load_extension(f'cogs.{file[:-3]}')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


async def main():
    await load()

asyncio.run(main())
client.run(os.environ.get('DISCORD_TOKEN'))