import os
import random
import data as d
import lyrics as l

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = d.DISCORD_TOKEN
GUILD = ""

bot = commands.Bot(command_prefix = "*")

@bot.event
async def on_ready():
    print(bot.user.name, "has connected to Discord!")

@bot.command(name = "ye", help = 'Responds with a random Kanye lyric')
async def kanye(ctx):
    response = random.choice(l.kanye_west_lyrics)
    await ctx.channel.send(response)

@bot.command(name = "drake", help = "Responds with a random Drake lyric")
async def drake(ctx):
    drakeLyric = random.choice(l.drake_lyrics)
    await ctx.channel.send(drakeLyric)

@bot.command(name = "wayne", help = "Responds with a random Lil Wayne lyric")
async def lilWayne(ctx):
    lWLyric = random.choice(l.lil_wayne_lyrics)
    await ctx.channel.send(lWLyric)

@bot.command(name = "rocky", help = "Responds with a random A$AP Rocky lyric")
async def rocky(ctx):
    rockyLyric = random.choice(l.asap_rocky_lyrics)
    await ctx.channel.send(rockyLyric)

@bot.command(name = "gambino", help = "Responds with a random Childish Gambino lyric")
async def gambino(ctx):
    gambinoLyric = random.choice(l.childish_gambino_lyrics)
    await ctx.channel.send(gambinoLyric)

@bot.command(name = "cudi", help = "Responds with a random Kid Cudi lyric")
async def cudi(ctx):
    cudiLyric = random.choice(l.kid_cudi_lyrics)
    await ctx.channel.send(cudiLyric)

@bot.command(name = "frank", help = "Responds with a random Frank Ocean lyric")
async def frank(ctx):
    frankLyric = random.choice(l.frank_ocean_lyrics)
    await ctx.channel.send(frankLyric)

@bot.command(name = "trash", help = "I don't know why she's here. If you like Doja Cat here's your lyric I guess")
async def trash(ctx):
    trashLyric = random.choice(l.doja_cat_lyrics)
    await ctx.channel.send(trashLyric)

@bot.command(name = "bye", help = "kills the bot :(")
async def death(ctx):
    await ctx.bot.logout()

bot.run(TOKEN)
