import random
import data as d
import lyrics_list as l

import discord
from discord.ext import commands

class Lyrics(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
        print("{botname} has connected to Discord!".format(bot.user))

    @commands.command(help = 'Responds with a random Kanye lyric')
    async def ye(self, ctx):
        response = random.choice(l.kanye_west_lyrics)
        embed = discord.Embed(
            color= 0xCFB997,
            title = "Kanye West Lyric",
            description = response
        )
        await ctx.send(embed = embed)

    @commands.command(name = "drake", help = "Responds with a random Drake lyric")
    async def drake(self, ctx):
        drakeLyric = random.choice(l.drake_lyrics)
        embed = discord.Embed(
            color= 0x1445cc,
            title = "Drake Lyric",
            description = drakeLyric
        )
        await ctx.send(embed=embed)

    @commands.command(name = "wayne", help = "Responds with a random Lil Wayne lyric")
    async def lilWayne(self, ctx):
        lWLyric = random.choice(l.lil_wayne_lyrics)
        embed = discord.Embed(
            color= 0xe35a24,
            title = "Lil Wayne Lyric",
            description = lWLyric
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name = "rocky", help = "Responds with a random A$AP Rocky lyric")
    async def rocky(self, ctx):
        rockyLyric = random.choice(l.asap_rocky_lyrics)
        embed = discord.Embed(
            color= 0x000000,
            title = "A$AP Rocky Lyric",
            description = rockyLyric
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name = "gambino", help = "Responds with a random Childish Gambino lyric")
    async def gambino(self, ctx):
        gambinoLyric = random.choice(l.childish_gambino_lyrics)
        embed = discord.Embed(
            color= 0x0ee844,
            title = "Childish Gambino Lyric",
            description = gambinoLyric
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name = "cudi", help = "Responds with a random Kid Cudi lyric")
    async def cudi(self, ctx):
        cudiLyric = random.choice(l.kid_cudi_lyrics)
        embed = discord.Embed(
            color= 0xecf026,
            title = "Kid Cudi Lyric",
            description = cudiLyric
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name = "frank", help = "Responds with a random Frank Ocean lyric")
    async def frank(self, ctx):
        frankLyric = random.choice(l.frank_ocean_lyrics)
        embed = discord.Embed(
            color= 0x781fcc,
            title = "Frank Ocean Lyric",
            description = frankLyric
        )
        await ctx.channel.send(embed=embed)

    @commands.command(name = "trash", help = "I don't know why she's here. If you like Doja Cat here's your lyric I guess")
    async def trash(self, ctx):
        trashLyric = random.choice(l.doja_cat_lyrics)
        embed = discord.Embed(
            color= 0xff00ea,
            title = "Doja Trash Lyric",
            description = trashLyric
        )
        await ctx.channel.send(embed=embed)

    @commands.command(help = "kills the bot :(")
    async def death(self, ctx):
        embed = discord.Embed(
            color= 0x59ffee,
            title = "bye meanie :(",
        )
        if True:
            await ctx.send(embed=embed)
            await ctx.bot.logout()
        else:
            return

def setup(bot):
    bot.add_cog(Lyrics(bot))
