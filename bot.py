# 67648
# NTcxNTQ5MDQyODQ1MTU1MzQ5.XMP0xA.hejIL6W8ZEKmq7X3dIH7qKc_lUM
# https://discordapp.com/api/oauth2/authorize?client_id=571549042845155349&permissions=0&scope=bot
# 534878922014457865
import discord
import urllib
from bs4 import BeautifulSoup
import requests

result,phrase,url,err = "","","",False

def extractData(command, message):
    global result, phrase, err, url
    definition = command.startswith("b!def")
    phrase = message.content[(6 if definition else 7):]
    err = False
    url = ("https://www.urbandictionary.com/define.php?term={}" if definition else "https://www.lyrics.com/lyrics/{}").format(phrase.replace(" ", "%20"))
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features="html.parser")
        result = soup.find("div", attrs={"class": "meaning"}).text.replace("&apos", "\'") if definition else soup.find_all("div", {"class": "sec-lyric clearfix"})
        embed = discord.Embed(title=("Urban Dictionary: " if definition else "Find song by lyric: ") + phrase,
                              description=result if definition else None,
                              inline=False,
                              color=0xecce8b)
        if not definition:
            for idx, val in zip(range(5), result):
                data = val.text.replace("&pos","\'").split("\n")
                embed.add_field(name = str(idx+1) + ". " + data[2], value="Artist: " + data[3], inline=False)
    except Exception as e:
        embed.title = "Error"
        embed.description = "The phrase you entered was not found!"
        embed.color = 0xff0000
    return embed

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as: {}\n{}\n------".format(self.user.name, self.user.id))
        game = discord.Game("with Hyebin and Deep")
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        # print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
        sentdex_guild = client.get_guild(message.guild.id)
            # client.get_guild(534878922014457865)
        if message.author.id == self.user.id: return
        elif "b!members" == message.content.lower(): await message.channel.send(f"```{sentdex_guild.member_count}```")
        elif "b!owner" == message.content.lower(): await message.channel.send(f"```{sentdex_guild.owner}```")
        elif "b!end" == message.content.lower(): await client.close()
        elif message.content.startswith('b!hello'): await message.channel.send('Hello {0.author.mention}'.format(message))
        elif "b!report" == message.content.lower():
            online = 0
            idle = 0
            offline = 0
            for m in sentdex_guild.members:
                if str(m.status) == "online": online += 1
                elif str(m.status) == "offline": offline += 1
                else: idle += 1
            await message.channel.send(f"``` Online: {online} \n Indle/Busy/Etc: {idle} \n Offline: {offline}```")
        elif "b!binton" == message.content.lower():
            file = discord.File("rere.jpg", filename="rere.jpg")
            await message.channel.send("Picture of Binton", file=file)
        elif "b!help" == message.content.lower():
            embed = discord.Embed(title="Hello I'm Binton Bot",
                                  description="Below you can see all the commands I know. \n If you wish to contact the real Binton add \"Binton#2193\" \n"
                                              "If you wish to contact Sriracha add \"Sriracha#9529\" he helped make this bot :3")

            embed.set_image(url="https://i.imgur.com/JUV5pEs.jpg")
            embed.add_field(name="b!owner", value="See owner of the server", inline=False)
            embed.add_field(name="b!members", value="Counts total members in the server", inline=False)
            embed.add_field(name="b!report", value="Display status of all the members", inline=False)
            embed.add_field(name="b!binton", value="Shows brief description of Binton", inline=False)
            embed.add_field(name="b!pic <@user>", value="Returns profile of a user", inline=False)
            embed.add_field(name="b!def <word>", value="Returns slang defintion of the word", inline=False)
            embed.add_field(name="b!song <lyric>", value="Looking for songs by the lyrics", inline=False)
            embed.add_field(name="b!lyrics <song>/<artist>", value="Finds the lyrics for the song by the artist", inline=False)
            embed.add_field(name="b!end", value="Temporarily Unavailable", inline=False)

            await message.channel.send(embed=embed)

        elif message.content.startswith("b!pic"):
            for member in message.mentions:
                embed = discord.Embed(title=str(member), description='{}, Nice profile picture!'.format(member), color=0xecce8b)
                embed.set_image(url=(member.avatar_url))
            await message.channel.send(embed=embed)

        elif message.content.startswith("b!def") or message.content.startswith("b!song"):
            await message.channel.send(embed=extractData(message.content, message))


        elif message.content.startswith("b!lyrics"):
            phrase = message.content[9:].split("/")
            url = (
                "https://lyrics.fandom.com/wiki/{}:{}").format(phrase[1].replace(" ", "_"), phrase[0].replace(" ", "_"))
            print(url)
            try:
                r = requests.get(url)
                soup = BeautifulSoup(r.content, features="html.parser")
                result = soup.find("div", attrs={"class": "lyricbox"})
                found = result is not None
                res = ""
                if found:
                    for x in result: res+= str(x).replace("<br/>","")+"\n" if str(x) == "<br/>" else str(x)
                embed = discord.Embed(title=("Lyrics for song: {}".format(phrase[0]) if found else "This song was not found"),
                                      description=res.replace('<div class="lyricsbreak"></div>',"") if found else None,
                                      inline=False,
                                      color=0xecce8b if found else 0xff0000)
            except Exception as e:
                embed.title = "Error"
                embed.description = "The song you entered was not found!"
                embed.color = 0xff0000

            await message.channel.send(embed=embed)


client = MyClient()
client.run('NTcxNTQ5MDQyODQ1MTU1MzQ5.XMP0xA.hejIL6W8ZEKmq7X3dIH7qKc_lUM')
