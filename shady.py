"""
Shady stuff to respond to messages and a simple timer
"""

import datetime
from discord.ext import tasks

utc2 = pytz.timezone()

times = [
    datetime.time(8, 55, tzinfo=utc2),
    datetime.time(9, 45, tzinfo=utc2),
    datetime.time(10, 35, tzinfo=utc2),
    datetime.time(11, 25, tzinfo=utc2),
    datetime.time(13, 10, tzinfo=utc2),
    datetime.time(13, 42, tzinfo=utc2)
]

test_times = []
for x in range(0,15):
    for y in range(0,60):
        test_times.append(datetime.time(x,y))

@tasks.loop(time=times)
async def timeloop(channel_out, test=False):
    """
    Posts messages at specific times
    Parameters:
        channel_out (discord.channel.TextChannel)
        test (bool) (optional)
    Returns:
        none
    Example:
        await timeloop.start(channel_out)
    """
    if not test:
        print(f"Reminder sent {datetime.datetime.now()}")
        await channel_out.send("Break time")
    else:
        print(f"channel_out: {channel_out} {type(channel_out)}")
        print(datetime.datetime.now())
        await channel_out.send("Test")

async def response(message, test_channel=None):
    """
    Message responses from shaderunner7
    Parameters:
        message (discord.message.Message)
        test_channel (discord.channel.TextChannel) (optional)
    Returns:
        none
    Example:
        await response(message)
    """
    username = str(message.author).split("#", maxsplit=1)[0]
    #channel = str(message.channel.name)
    user_message = str(message.content)

    if username == "shaderunner7":
        pass
        print(f"Master {username}")
    else:
        return

    match user_message:
        case "Hi":
            await message.channel.send("Hi")
        case "Give time":
            await message.channel.send(
                f"It's {datetime.datetime.now()}")
        case "Reminder test":
            await test_channel.send("Reminder test")
            await timeloop(test_channel, True)
        case _:
            return
