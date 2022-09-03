import discord
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents) # this is the object for the discord Client library

PREFIX = '!'

# this is called whenever the bot is turned on AND 'ready'
@client.event 
async def on_ready():
  print('Hi this is me')

# this is called whenever the bot receives a message
@client.event
async def on_message(message):
  if message.content[0] == PREFIX:
    msg = message.content[1:].split(' ') # msg is basically the actual contents of the command. ie: !asdf, msg = asdf

    if msg == "hello":
      await message.channel.send('Hello!')

client.run(DISCORD_TOKEN)
  # elif message.author == client.user:
  #   return