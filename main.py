"""
Main bot script
"""

import os
import datetime
import json
from dotenv import load_dotenv
import discord
import shady

load_dotenv()
client = discord.Client(intents=discord.Intents.all())
path = __file__.removesuffix(os.path.basename(__file__))
with open(f"{path}channels.json", "r") as file:
    channels = json.load(file)

@client.event
async def on_ready():
    """Ready event"""
    print(f"{client.user} has connected to Discord")

    for channel in channels.items():
        if not isinstance(channel[1], int):
            print("Channels already set")
            break
        if client.get_channel(channel[1]) is None:
            print(f"Channel {channel[0]} not found")
            continue
        channels[channel[0]] = client.get_channel(channel[1])

    try:
        #await shady.timeloop.start(channels["general"])
        await shady.timeloop.start(channels["bot-testing"])
    except RuntimeError:
        print("Already running")
    #await shady.timeloop.start(channels["bot-testing"], True)
    #print(type(channels["bot-testing"]))

@client.event
async def on_resumed():
    """When resuming process"""
    print(f"Back online at {datetime.datetime.now()}")

@client.event
async def on_message(message):
    """Message events"""
    await shady.response(message, channels["bot-testing"])

client.run(os.getenv('DISCORD_TOKEN'))
