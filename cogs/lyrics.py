import random
import data as d
import lyrics_list as l
import datetime as dt
from datetime import datetime
import discord
from discord.ext import commands

class Lyrics(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = 'Responds with a random Kanye lyric')
    async def ye(self, ctx):
        response = random.choice(l.kanye_west_lyrics)
        embed = discord.Embed(
            color= 0xCFB997,
            title = "Kanye West Lyric",
            description = response,
            timestamp = datetime.today() + dt.timedelta(hours = 7)
        )
        await ctx.send(embed = embed)

    @commands.command(name = "drake", help = "Responds with a random Drake lyric")
    async def drake(self, ctx):
        drakeLyric = random.choice(l.drake_lyrics)
        embed = discord.Embed(
            color= 0x1445cc,
            title = "Drake Lyric",
            description = drakeLyric,
            timestamp = datetime.today() + dt.timedelta(hours = 7)
        )
        await ctx.send(embed=embed)

    @commands.command(name = "wayne", help = "Responds with a random Lil Wayne lyric")
    async def lilWayne(self, ctx):
        lWLyric = random.choice(l.lil_wayne_lyrics)
        embed = discord.Embed(
            color= 0xe35a24,
            title = "Lil Wayne Lyric",
            description = lWLyric,
            timestamp = datetime.today() + dt.timedelta(hours = 7)
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name = "rocky", help = "Responds with a random A$AP Rocky lyric")
    async def rocky(self, ctx):
        rockyLyric = random.choice(l.asap_rocky_lyrics)
        embed = discord.Embed(
            color= 0x000000,
            title = "A$AP Rocky Lyric",
            description = rockyLyric,
            timestamp = datetime.today() + dt.timedelta(hours = 7)
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name = "gambino", help = "Responds with a random Childish Gambino lyric")
    async def gambino(self, ctx):
        gambinoLyric = random.choice(l.childish_gambino_lyrics)
        embed = discord.Embed(
            color= 0x0ee844,
            title = "Childish Gambino Lyric",
            description = gambinoLyric,
            timestamp = datetime.today() + dt.timedelta(hours = 7)
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name = "cudi", help = "Responds with a random Kid Cudi lyric")
    async def cudi(self, ctx):
        cudiLyric = random.choice(l.kid_cudi_lyrics)
        embed = discord.Embed(
            color= 0xecf026,
            title = "Kid Cudi Lyric",
            description = cudiLyric,
            timestamp = datetime.today() + dt.timedelta(hours = 7)
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name = "frank", help = "Responds with a random Frank Ocean lyric")
    async def frank(self, ctx):
        frankLyric = random.choice(l.frank_ocean_lyrics)
        embed = discord.Embed(
            color= 0x781fcc,
            title = "Frank Ocean Lyric",
            description = frankLyric,
            timestamp = datetime.today() + dt.timedelta(hours = 7)
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name = "trash", help = "I don't know why she's here. If you like Doja Cat here's your lyric I guess")
    async def trash(self, ctx):
        trashLyric = random.choice(l.doja_cat_lyrics)
        embed = discord.Embed(
            color= 0xff00ea,
            title = "Doja Trash Lyric",
            description = trashLyric,
            timestamp = datetime.today() + dt.timedelta(hours = 7)
        )
        await ctx.channel.send(embed=embed)

    @commands.command(help = "kills the bot :(")
    async def death(self, ctx):
        await ctx.send("bye meanie :(" if ctx.author.name == "akniight" else "u aren't cool enough to shut me down :)")
        if ctx.author.name == "akniight":
            await ctx.bot.logout()

def setup(bot):
    bot.add_cog(Lyrics(bot))
