import os
import discord
#import random
from dotenv import load_dotenv
from shady import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

@client.event
async def on_message(message):
    channel = str(message.channel.name)
    """
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    """

    #print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

    if channel == "bot":
        await HelloWorld(message)

client.run(TOKEN)