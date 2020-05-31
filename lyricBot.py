import os
import random
import data

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = data.DISCORD_TOKEN
GUILD = ""

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name, "has connected to Discord!")

@client.event
async def on_member_arrival(member):
    await member.create_dm()
    await member.dm_channel.send("Hi", member.user, "did you get this message onna gang")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    ye_lyrics = data.kanye_west_lyrics
    if message.content == "-ye":
        response = random.choice(ye_lyrics)
        await message.channel.send(response)

client.run(TOKEN)
