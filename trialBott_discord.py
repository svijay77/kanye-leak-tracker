import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = ""
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
    kanye_west_lyrics = ['I made that b faaamous', 'He just mad cuz he can\'t get kanye fresh', 'Now I ain\'t saying that she a gold digger...', 'A n-word\'s money is homo, it\'s hard to get straight']
    if message.content.lower() == "-ye lyric":
        response = random.choice(kanye_west_lyrics)
        await message.channel.send(response)

client.run(TOKEN)
