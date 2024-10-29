import discord

async def HelloWorld(message):    
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    if username == "shaderunner7":
        print(f"Hello {username}")

    if user_message == "Hi":
        await message.channel.send(f"Hello there")