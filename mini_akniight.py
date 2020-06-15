import data as d
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = d.DISCORD_TOKEN
GUILD = ""

bot = commands.Bot(command_prefix = ".")

@bot.command(help = "Loads a cog of your choice")
async def load(ctx, extension):
    bot.load_extension("cogs.{}".format(extension))

@bot.command(help = "Reloads a cog of your choice")
async def reload(ctx, extension):
    bot.unload_extension("cogs.{}".format(extension))
    bot.load_extension("cogs.{}".format(extension))

bot.run(TOKEN)
