"""Shady stuff to respond to messages and
a simple timer
"""

import datetime
from discord.ext import tasks

times = [
    datetime.time(8, 45),
    datetime.time(9, 40),
    datetime.time(10, 40),
    datetime.time(11, 30),
    datetime.time(13, 40)
]

for x in range(0, 15):
    for y in range(0, 60, 5):
        times.append(datetime.time(x, y))

@tasks.loop(time=times)
async def timeloop(message):
    """Setting alarm time"""
    #clock_is = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)
    #print(f"Working on {message.channel}, {clock_is}")
    #if clock_is in times:
    print("Reminder sent")
    await message.channel.send(f"It's {datetime.datetime.now().time()}")

async def response(message):
    """Message responses from shaderunner7"""
    username = str(message.author).split("#", maxsplit=1)[0]
    #channel = str(message.channel.name)
    user_message = str(message.content)

    if username == "shaderunner7":
        print(f"Master {username}")
    else:
        return

    match user_message:
        case "Hi":
            await message.channel.send("Hi")
        case "Give time":
            await message.channel.send(
                f"It's {datetime.datetime.now()}, and times[0] is {times[0]}")
        case "Set reminders":
            await message.channel.send("Reminders test started?")
            print("Match case maybe?")
            await timeloop.start(message)
        case _:
            return
