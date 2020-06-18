import discord
import random
from random import Random
import gspread
import datetime as dt
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
Client = gspread.service_account(filename = 'D:\pythonProjects\discordBot/client_secret.json')

sh = Client.open("Copy of Kanye Unreleased Tracker")
sheet = sh.sheet1

def albumPicker(album):
    album_cover = ""

    if album == "Before College Dropout":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852588550783062/image0.jpg"
    elif album == "College Dropout":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852588777013328/image1.jpg"
    elif album == "Late Registration":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852588970082375/image2.jpg"
    elif album == "Graduation":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852589209026590/image3.jpg"
    elif album == "808s & Heartbreak":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852589435519046/image4.jpg"
    elif album == "MBDTF":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852589641302066/image5.jpg"
    elif album == "Watch The Throne":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852589808812102/image6.jpg"
    elif album == "Cruel Summer":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852590073053205/image7.jpg"
    elif album == "Yeezus":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852590345945088/image8.png"
    elif album == "So Help Me God":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852590601666630/image9.jpg"
    elif album == "The Life Of Pablo":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852640522272898/image0.jpg"
    elif album == "Cruel Winter":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852640748896276/image1.jpg"
    elif album == "TurboGrafx16":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852641059143680/image2.png"
    elif album == "ye":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852642011119616/image4.jpg"
    elif album == "Kids See Ghosts":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852642237612032/image5.jpg"
    elif album == "Good Ass Job":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852641713455174/image3.jpg"
    elif album == "Yandhi":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721913067650416710/yandhi.jpg"
    elif album == "Jesus Is King":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852642489401825/image6.jpg"
    elif album == "Jesus Is King II":
        album_cover = "https://cdn.discordapp.com/attachments/715392517448663093/721852642665431090/image7.jpg"
    else:
        pass

    return album_cover

class Leaks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Returns a random Kanye West Leak from before College Dropout to Jesus is King II.")
    async def kanyeleak(self, ctx):

        r = random.Random()
        location = str(r.randint(2, 489))
        print(location)

        era = "**"+str(sheet.acell('A1').value)+"**"
        era_value = str(sheet.acell('A' + location).value)
        names = "**"+str(sheet.acell('B1').value)+"**"
        names_value = str(sheet.acell('B' + location).value)
        notes = "**"+str(sheet.acell('C1').value)+"**"
        notes_value = str(sheet.acell('C' + location).value)
        leak_date = "**" + str(sheet.acell('D1').value + "**")
        leak_date_value = "No data available" if str(sheet.acell('D' + location).value) == "" else str(sheet.acell('D' + location).value)
        type = "**"+str(sheet.acell('E1').value)+"**"
        type_value = str(sheet.acell('E' + location).value)
        link = "**"+str(sheet.acell('H1').value)+"**"
        link_value = "No link available" if str(sheet.acell('H' + location).value) == "" else str(sheet.acell('H' + location).value)

        embed = discord.Embed(
            title = "Kanye West Leak",
            colour = 0xCFB997,
            timestamp = datetime.today() + dt.timedelta(hours = 7)
        )
        embed.set_thumbnail(
        url = albumPicker(era_value)
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
        await ctx.send(embed=embed)

    @commands.command(help = "Kanye Leaks from pre-College Dropout to Jesus is King 2... \n\n2-15: Before College Dropout \n16-40: College Dropout \n41-54: Late Registration \n55-75: Graduation \n76-94: 808s & Heartbreak \n95-130: MBDTF \n131-138: Watch the Throne \n139-149: Cruel Summer \n150-181: Yeezus \n182-226: So Help Me God \n227-308: The Life of Pablo \n309-316: Cruel Winter \n317-341: TurboGrafx16 \n342-372: ye \n373-379: Kids See Ghosts \n380-383: Good Ass Job \n384-455: Yandhi \n456-482: Jesus is King \n483-489: Jesus Is King II")

    async def yeleak(self, ctx, location):

        era = "**"+str(sheet.acell('A1').value)+"**"
        era_value = str(sheet.acell('A' + location).value)
        names = "**"+str(sheet.acell('B1').value)+"**"
        names_value = str(sheet.acell('B' + location).value)
        notes = "**"+str(sheet.acell('C1').value)+"**"
        notes_value = str(sheet.acell('C' + location).value)
        leak_date = "**" + str(sheet.acell('D1').value + "**")
        leak_date_value = "No data available" if str(sheet.acell('D' + location).value) == "" else str(sheet.acell('D' + location).value)
        type = "**"+str(sheet.acell('E1').value)+"**"
        type_value = str(sheet.acell('E' + location).value)
        link = "**"+str(sheet.acell('H1').value)+"**"
        link_value = "No link available" if str(sheet.acell('H' + location).value) == "" else str(sheet.acell('H' + location).value)

        album_cover = albumPicker(era_value)

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
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Leaks(bot))
