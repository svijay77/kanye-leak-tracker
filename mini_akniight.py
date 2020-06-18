import data as d
import discord
from dotenv import load_dotenv
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials



load_dotenv()
TOKEN = d.DISCORD_TOKEN

bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print("{} has connected to discord!".format(bot.user))
    await bot.change_presence(activity = discord.Game("admiring Kanye West"))
    bot.load_extension("cogs.leaks")
    bot.load_extension("cogs.lyrics")

@bot.command(help = "Reloads a cog of your choice")
async def reload(ctx, extension):
    bot.unload_extension("cogs.{}".format(extension))
    bot.load_extension("cogs.{}".format(extension))
    await ctx.send("{} has been reloaded!".format(extension))

bot.run(TOKEN)
