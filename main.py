"""Main bot script"""

import os
import datetime
from dotenv import load_dotenv
import discord
#from discord.ext import tasks
import shady

load_dotenv()
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    """Ready event"""
    print(f"{client.user} has connected to Discord")
    #await shady.MyClient.setup_hook(client)
    #await shady.timeloop.start()

@client.event
async def on_message(message):
    """Message events"""
    await shady.HelloWorld(message)

client.run(os.getenv('DISCORD_TOKEN'))
