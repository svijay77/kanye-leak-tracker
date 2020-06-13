import os
import random
import data as d
import lyrics as l

import discord
import gspread
from dotenv import load_dotenv
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials


load_dotenv()
TOKEN = d.DISCORD_TOKEN
GUILD = ""

bot = commands.Bot(command_prefix = ".")



@bot.event
async def on_ready():
    print(bot.user.name, "has connected to Discord!")

@bot.command(help = 'Responds with a random Kanye lyric', category = "Lyrics")
async def ye(ctx):
    response = random.choice(l.kanye_west_lyrics)
    embed = discord.Embed(
        color= 0xCFB997,
        title = "Kanye West Lyric",
        description = response
    )
    await ctx.send(embed = embed)

@bot.command(name = "drake", help = "Responds with a random Drake lyric", category = "Lyrics")
async def drake(ctx):
    drakeLyric = random.choice(l.drake_lyrics)
    embed = discord.Embed(
        color= 0x1445cc,
        title = "Drake Lyric",
        description = drakeLyric
    )
    await ctx.send(embed=embed)

@bot.command(name = "wayne", help = "Responds with a random Lil Wayne lyric", category = "Lyrics")
async def lilWayne(ctx):
    lWLyric = random.choice(l.lil_wayne_lyrics)
    embed = discord.Embed(
        color= 0xe35a24,
        title = "Lil Wayne Lyric",
        description = lWLyric
    )
    await ctx.channel.send(embed=embed)

@bot.command(name = "rocky", help = "Responds with a random A$AP Rocky lyric", category = "Lyrics")
async def rocky(ctx):
    rockyLyric = random.choice(l.asap_rocky_lyrics)
    embed = discord.Embed(
        color= 0x000000,
        title = "A$AP Rocky Lyric",
        description = rockyLyric
    )
    await ctx.channel.send(embed=embed)

@bot.command(name = "gambino", help = "Responds with a random Childish Gambino lyric", category = "Lyrics")
async def gambino(ctx):
    gambinoLyric = random.choice(l.childish_gambino_lyrics)
    embed = discord.Embed(
        color= 0x0ee844,
        title = "Childish Gambino Lyric",
        description = gambinoLyric
    )
    await ctx.channel.send(embed=embed)

@bot.command(name = "cudi", help = "Responds with a random Kid Cudi lyric", category = "Lyrics")
async def cudi(ctx):
    cudiLyric = random.choice(l.kid_cudi_lyrics)
    embed = discord.Embed(
        color= 0xecf026,
        title = "Kid Cudi Lyric",
        description = cudiLyric
    )
    await ctx.channel.send(embed=embed)

@bot.command(name = "frank", help = "Responds with a random Frank Ocean lyric", category = "Lyrics")
async def frank(ctx):
    frankLyric = random.choice(l.frank_ocean_lyrics)
    embed = discord.Embed(
        color= 0x781fcc,
        title = "Frank Ocean Lyric",
        description = frankLyric
    )
    await ctx.channel.send(embed=embed)

@bot.command(name = "trash", help = "I don't know why she's here. If you like Doja Cat here's your lyric I guess", category = "Lyrics")
async def trash(ctx):
    trashLyric = random.choice(l.doja_cat_lyrics)
    embed = discord.Embed(
        color= 0xff00ea,
        title = "Doja Trash Lyric",
        description = trashLyric
    )
    await ctx.channel.send(embed=embed)

@bot.command(help = "kills the bot :(", category = "System commands")
async def death(ctx):
    embed = discord.Embed(
        color= 0x59ffee,
        title = "bye",
    )
    if True:
        await ctx.send(embed=embed)
        await ctx.bot.logout()
    else:
        return

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
Client = gspread.service_account(filename = 'D:\pythonProjects\discordBot/client_secret.json')

sh = Client.open("Copy of Kanye Unreleased Tracker")
info = sh.sheet1.get('A1:B2')

@bot.event
async def on_ready():
    print(bot.user.name, "has connected to Discord!")

@bot.command(aliases = ["ye leak"], help = "Gives a list of dates from Kanye leaks", category = "Leaks")
async def ye_leak(ctx):
    embed = discord.Embed(
        colour = 0x000000
    )
    embed.set_author(
        name = 'User: {author}'.format(author = ctx.author),
        icon_url = ""
    )
    embed.add_field( #era
    name = "**"+str(sh.sheet1.acell('A1').value)+"**",
    value = str(sh.sheet1.acell('A244').value),
    )
    embed.add_field( #name
    name = "**"+str(sh.sheet1.acell('B1').value)+"**",
    value = str(sh.sheet1.acell('B244').value),
    inline = True
    )
    embed.add_field( #leak date
    name = "**" + str(sh.sheet1.acell('D1').value + "**"),
    value = "No data available", #str(sh.sheet1.acell('D244').value),
    inline = False
    )
    embed.add_field( #link
    name = "**"+str(sh.sheet1.acell('H1').value)+"**",
    value = str(sh.sheet1.acell('H244').value),
    inline = False
)
    await ctx.send(embed=embed)

bot.run(TOKEN)
