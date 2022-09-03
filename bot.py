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
        if(len(msg) >=1):
          args = msg[1:]

        if command == "hello":
            await message.channel.send('Hello!')

        if command == "askQuestion":
            # data = 
            data = await getReq(message)
            dataLen = len(data)
            index = random.randint(0,dataLen)
            await message.channel.send(data[index]['ImageLink']) # this is the link to the image randomly choose object
            await message.channel.send('what is this?')
            # ans = data[index]['name'] is the answer to the question 
            # response == ans 
            # send a message to the user saying if they got it right or wrong, exit while loop,
            # and once everything is finished work on leaderboard

# gets data from the server and store into memory


async def getReq(message):
    URL = 'http://localhost:3000/api/getAll'  # url of the api where you're going to import
    response = requests.get(URL)
    # later test for response.status_code works, prob dont have to but its good practice
    print(response.status_code)
    return response.json()
    

client.run(DISCORD_TOKEN)
