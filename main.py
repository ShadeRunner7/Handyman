"""
Main bot script
"""

import os
from dotenv import load_dotenv
import discord
import shady

load_dotenv()
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    """Ready event"""
    print(f"{client.user} has connected to Discord")

@client.event
async def on_message(message):
    """Message events"""
    print(type(message))
    await shady.response(message)

client.run(os.getenv('DISCORD_TOKEN'))
