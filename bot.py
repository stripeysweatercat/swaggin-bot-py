import discord
import asyncio
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
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

async def main():
    await load()

asyncio.run(main())
client.run(os.getenv('MTAzNDczMTQ2NTY1ODg2NzgwNQ.GW63JZ.d6anCiFiT_f7upEHiTaMgn720mWRo03N37kdts'))