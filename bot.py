
# 67648
# NTcxNTQ5MDQyODQ1MTU1MzQ5.XMP0xA.hejIL6W8ZEKmq7X3dIH7qKc_lUM
# https://discordapp.com/api/oauth2/authorize?client_id=571549042845155349&permissions=0&scope=bot
# 534878922014457865
import discord
import urllib
from bs4 import BeautifulSoup
import requests


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        game = discord.Game("with Hyebin")
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        # print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
        sentdex_guild = client.get_guild(message.guild.id)
            # client.get_guild(534878922014457865)
        if message.author.id == self.user.id:
            return
        elif "b!members" == message.content.lower():
            await message.channel.send(f"```{sentdex_guild.member_count}```")
        elif "b!owner" == message.content.lower():
            await message.channel.send(f"```{sentdex_guild.owner}```")
        elif "b!end" == message.content.lower():
            await client.close()
        elif message.content.startswith('b!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        elif "b!report" == message.content.lower():
            online = 0
            idle = 0
            offline = 0
            for m in sentdex_guild.members:
                if str(m.status) == "online":
                    online += 1
                if str(m.status) == "offline":
                    offline += 1
                else:
                    idle += 1
            await message.channel.send(f"``` Online: {online} \n Indle/Busy/Etc: {idle} \n Offline: {offline}```")
        elif "b!binton" == message.content.lower():
            file = discord.File("rere.jpg", filename="rere.jpg")
            await message.channel.send("Picture of Binton", file=file)
        elif "b!help" == message.content.lower():
            embed = discord.Embed(title="Hello I'm Binton Bot",
                                  description="Below you can see all the commands I know. \n If you wish to contact the real Binton add \"Binton#2193\" \n"
                                              "\"Sriracha#9529\" helped me make this bot :3")

            embed.set_image(url="https://i.imgur.com/JUV5pEs.jpg")
            embed.add_field(name="b!owner", value="See owner of the server", inline=False)
            embed.add_field(name="b!members", value="Counts total members in the server", inline=False)
            embed.add_field(name="b!report", value="Display status of all the members", inline=False)
            embed.add_field(name="b!binton", value="Shows brief description of Binton", inline=False)
            embed.add_field(name="b!pic <@user>", value="Returns profile of a user", inline=False)
            embed.add_field(name="b!def <word>", value="Returns slang defintion of the word", inline=False)
            embed.add_field(name="b!end", value="Temporarily Unavailable", inline=False)
            await message.channel.send(message.channel, embed=embed)

        elif message.content.startswith("b!pic"):
            for member in message.mentions:
                pfp = member.avatar_url
                embed = discord.Embed(title=str(member), description='{}, Nice profile picture!'.format(member), color=0xecce8b)
                embed.set_image(url=(pfp))
            await message.channel.send(message.channel, embed=embed)

        elif message.content.startswith("b!def"):
            phrase = message.content[6:]
            err = False
            url ="https://www.urbandictionary.com/define.php?term={}".format(phrase.replace(" ", "%20"))
            try:
                r = requests.get("https://www.urbandictionary.com/define.php?term={}".format(phrase.replace(" ", "%20")))
                soup = BeautifulSoup(r.content,features="html.parser")
                result = soup.find("div", attrs={"class": "meaning"}).text.replace("&apos","\'")
            except Exception as e:
                phrase = "Error"
                result = "The phrase you entered was not found!"
                err = True

            embed = discord.Embed(title="Urban Dictionary : "+ phrase,description = result, inline = False ,url = url,  color=0xecce8b if not err else 0xff0000)
            #embed.add_field(name=phrase+":", value=result, inline=False)
            print(url)
            await message.channel.send(message.channel, embed=embed)
        elif message.content.startswith("b!song"):
            name = message.content[7:]
            err2 = False
            try :
                b = requests.get("https://www.lyrics.com/lyrics/{}".format(name.replace(" ","%20")))
                soup2 = BeautifulSoup (b.content,features="html.parser")
                resultSet = soup2.find_all("div",{"class":"sec-lyric clearfix"})
                counter = 1
                embed = discord.Embed(title="Find song by lyric: ", description = "\" "+ name+"\"", inline = False ,  color=0xecce8b if not err2 else 0xff0000)
                for i in resultSet :
                    blah = i.text.replace("&apos","'")
                    nameOfSong = blah.split("\n")[2]
                    artist = blah.split("\n")[3]
                    embed.add_field(name = str(counter)+". "+nameOfSong ,value = "by artist:   "+artist, inline= False)
                    if counter == 3 :
                        break

                    counter = counter +1
            except Exception as e:
                name = "Error"
                artist = e
                print(e)
                err2 = True
            #nameOfSong = result2.split("\n")[2]
            #artist = result2.split("\n")[3]
            #print(type(result2))
           
            #embed.add_field(name = "1. "+nameOfSong +" by artist ",value = artist, inline= False)
            await message.channel.send(message.channel, embed= embed)

client = MyClient()
client.run('NTcxNTQ5MDQyODQ1MTU1MzQ5.XMP0xA.hejIL6W8ZEKmq7X3dIH7qKc_lUM')