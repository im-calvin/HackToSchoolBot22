import discord
import os
import random
from dotenv import load_dotenv
import requests

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
# this is the object for the discord Client library
client = discord.Client(intents=intents)

PREFIX = '!'

# this is called whenever the bot is turned on AND 'ready'


@client.event
async def on_ready():
    print('Hi this is me')

# this is called whenever the bot receives a message


@client.event
async def on_message(message):
    if message.content[0] == PREFIX:
        # msg is basically the actual contents of the command. ie: !asdf, msg = asdf
        msg = message.content[1:].split(' ')
        # command is the first word from the msg string
        command = msg[0].strip()
        args = msg[1].strip()

        if command == "hello":
            await message.channel.send('Hello!')

        if command == "askQuestion":
            data = getReq()
            len = data.length
            await message.channel.send(data[random.randint(0,len)]['ImageLink']) # this is the link to the image randomly choose object
            await message.channel.send('what is this?')
# gets data from the server and store into memory


async def getReq():
    URL = ''  # url of the api where you're going to import
    response = await requests.get(URL)
    print(response.json())
    return response.json
    

client.run(DISCORD_TOKEN)
