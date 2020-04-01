import os.path
import discord


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    
    if(message.content == ".scrape"):
        channels = client.private_channels
        for channel in channels:
            if isinstance(channel, discord.DMChannel):
                   file = open(f"{channel.recipient.id}.txt", "w+", encoding="utf-8")
                   async for message in channel.history(limit=9999):
                       file.write(f"{message.author.name}#{message.author.discriminator}: {message.content}\r\n")





client.run('your token', bot=False)
