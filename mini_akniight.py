import os
import random
import time
import data as d
import lyrics as l

import discord
import gspread
import datetime as dt
from datetime import datetime
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

@bot.command(help = "Kanye Leaks from pre-College Dropout to Jesus is King 2", category = "Leaks")
async def leak(ctx, *, location):

    era = "**"+str(sh.sheet1.acell('A1').value)+"**"
    era_value = str(sh.sheet1.acell('A' + location).value)
    names = "**"+str(sh.sheet1.acell('B1').value)+"**"
    names_value = str(sh.sheet1.acell('B' + location).value)
    notes = "**"+str(sh.sheet1.acell('C1').value)+"**"
    notes_value = str(sh.sheet1.acell('C' + location).value)
    leak_date = "**" + str(sh.sheet1.acell('D1').value + "**")
    leak_date_value = "No data available" if str(sh.sheet1.acell('D' + location).value) == "" else str(sh.sheet1.acell('D' + location).value)
    type = "**"+str(sh.sheet1.acell('E1').value)+"**"
    type_value = str(sh.sheet1.acell('E' + location).value)
    link = "**"+str(sh.sheet1.acell('H1').value)+"**"
    link_value = str(sh.sheet1.acell('H' + location).value)

    album_cover = ""

    if era_value == "Before College Dropout":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852588550783062/image0.jpg"
    elif era_value == "College Dropout":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852588777013328/image1.jpg"
    elif era_value == "Late Registration":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852588970082375/image2.jpg"
    elif era_value == "Graduation":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852589209026590/image3.jpg"
    elif era_value == "808s & Heartbreak":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852589435519046/image4.jpg"
    elif era_value == "MBDTF":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852589641302066/image5.jpg"
    elif era_value == "Watch The Throne":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852589808812102/image6.jpg"
    elif era_value == "Cruel Summer":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852590073053205/image7.jpg"
    elif era_value == "Yeezus":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852590345945088/image8.png"
    elif era_value == "So Help Me God":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852590601666630/image9.jpg"
    elif era_value == "The Life Of Pablo":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852640522272898/image0.jpg"
    elif era_value == "Cruel Winter":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852640748896276/image1.jpg"
    elif era_value == "TurboGrafx16":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852641059143680/image2.png"
    elif era_value == "ye":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852642011119616/image4.jpg"
    elif era_value == "Kids See Ghosts":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852642237612032/image5.jpg"
    elif era_value == "Good Ass Job":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852641713455174/image3.jpg"
    elif era_value == "Yandhi":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721913067650416710/yandhi.jpg"
    elif era_value == "Jesus Is King":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852642489401825/image6.jpg"
    else:
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852642665431090/image7.jpg"


    embed = discord.Embed(
        title = "Kanye West Leak",
        colour = 0xCFB997,
        timestamp = datetime.today() + dt.timedelta(hours = 7)
    )
    embed.set_thumbnail(
    url = album_cover
    )
    embed.set_author(
        name = 'user: {author}'.format(author = ctx.author),
        icon_url = str(ctx.author.avatar_url)
    )
    embed.add_field( #era
        name = era ,
        value = era_value
    )
    embed.add_field( #name
        name = names,
        value = names_value
    )
    embed.add_field( #notes
        name = notes,
        value = notes_value,
        inline = False
    )
    embed.add_field( #leak date
        name = leak_date,
        value = leak_date_value
    )
    embed.add_field( #type
        name = type,
        value = type_value
    )
    embed.add_field( #link
        name = link ,
        value = link_value,
        inline = False
    )
    print(len(embed))
    await ctx.send(embed=embed)

bot.run(TOKEN)
