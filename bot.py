import discord
import os
import random
import asyncio
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
    if message.author == client.user:
        return

    if message.content[0] == PREFIX:
        # msg is basically the actual contents of the command. ie: !asdf, msg = asdf
        msg = message.content[1:].split(' ')
        # command is the first word from the msg string
        command = msg[0].strip().lower()
        if (len(msg) >= 1):
            args = msg[1:]

        if command == "hello":
            await message.channel.send('Hello!')

        if command == 'help':
            await message.channel.send('Documentation does not exist at this moment. Have a nice day!')

        if command == "askquestion" or command == 'askq':
            # data =
            await message.channel.send('Respond with one of the following difficulities:\n(Easy/Medium/Hard/Any)')
            try:
                x = False
                while (x == False):
                    currMSG = await client.wait_for('message', timeout=60.0)
                    cleanMSG = currMSG.content.strip().lower()
                    try:
                        if (cleanMSG == "easy") or (cleanMSG == "medium") or (cleanMSG == "hard") or (cleanMSG == "any"):
                            difficulty = cleanMSG
                            x = True
                            await askQuestion(message, difficulty)

                        else:
                            await message.channel.send('Invalid Input')

                    except:
                        await message.channel.send('Invalid Input')

            except asyncio.TimeoutError:
                await message.channel.send("You took too long to respond")


# gets data from the server and store into memory


async def getALL(message):
    # url of the api where you're going to import
    URL = 'http://localhost:3000/api/organic_compounds'
    response = requests.get(URL)

    return response.json()


async def getFromDifficulty(message, difficulty):
    URL = 'http://localhost:3000/api/organic_compounds/' + difficulty
    response = requests.get(URL)

    return response.json()


async def askQuestion(message, difficulty):

    if (difficulty == "any"):
        data = await getALL(message)

    else:
        data = await getFromDifficulty(message, difficulty)

    dataLen = len(data)
    index = random.randint(0, dataLen)
    answer = data[index]['Name'].strip().lower()
    # this is the link to the image randomly choose object
    await message.channel.send(data[index]['ImageLink'])
    await message.channel.send('what is this? (respond in form of "answer")')

    try:
        currMSG = await client.wait_for('message', timeout=60.0)
        cleanMSG = currMSG.content.strip().lower()

        if cleanMSG == answer:
            await message.channel.send('Correct!')
            # update scores/database

        elif cleanMSG == 'quit':
            await message.channel.send('You suck')

    except asyncio.TimeoutError:
        await message.channel.send('Timeout')


client.run(DISCORD_TOKEN)
