import discord
import gspread
import datetime as dt
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials

class Leaks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Kanye Leaks from pre-College Dropout to Jesus is King 2... \n\n2-15: Before College Dropout \n16-40: College Dropout \n41-54: Late Registration \n55-75: Graduation \n76-94: 808s & Heartbreak \n95-130: MBDTF \n131-138:Watch the Throne \n139-149: Cruel Summer \n150-181: Yeezus \n182-226: So Help Me God \n227-308: The Life of Pablo \n309-316: Cruel Winter \n317-341: TurboGrafx16 \n342-372: ye \n373-379: Kids See Ghosts \n380-383: Good Ass Job \n384-455: Yandhi \n456-482: Jesus is King \n483-489: Jesus Is King II")

    async def leak(self, ctx, *, location):

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        Client = gspread.service_account(filename = 'D:\pythonProjects\discordBot/client_secret.json')

        sh = Client.open("Copy of Kanye Unreleased Tracker")

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
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Leaks(bot))
