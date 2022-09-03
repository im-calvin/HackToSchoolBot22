import discord
import os
import random
from dotenv import load_dotenv
import requests
import io
import aiohttp

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
            await message.channel.send(decodeImg) # this is the link to the image randomly choose object
            await message.channel.send('what is this?')

            # ans = data[index]['name'] is the answer to the question 
            # response == ans 
            # send a message to the user saying if they got it right or wrong, exit while loop,
            # and once everything is finished work on leaderboard


# gets data from the server and store into memory


async def getReq():
    URL = ''  # url of the api where you're going to import
    response = requests.get(URL)
    print(response.json())
    return response.json

# decodes image url 
async def decodeImg(message, datalist):

    length = len(datalist)
    index = random.randint(0,length)

    async with aiohttp.ClientSession() as session:
        async with session.get(data[index]['ImageLink']) as resp:
            if resp.status != 200:
                return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'cool_image.png'))
    



client.run(DISCORD_TOKEN)
