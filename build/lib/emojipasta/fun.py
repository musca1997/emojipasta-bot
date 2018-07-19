from random import choice
from random import randint
import discord
import asyncio
import json
import requests
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from emojigene import EmojipastaGenerator
from bs4 import BeautifulSoup

class Fun():

    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 8, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def sheriff(self, ctx, emo: str=None):
        sheriff = "⠀ ⠀ ⠀   🤠\n　   {}{}{}\n    {}   {}　{}\n  👇  {}{}  👇\n  　  {}　{}\n　   {}　 {}\n　    👢     👢".format(emo, emo, emo, emo, emo, emo, emo, emo, emo, emo, emo, emo)
        await self.client.say(sheriff + "\nDid someone call the sheriff of " + emo + "?")

    @commands.command(pass_context=True)
    async def theguy(self, ctx, emo:str=None):
        if emo is None:
            theguy = """:ok_hand:             :weary:
    :eggplant: :zzz: :necktie: :eggplant:
                    :oil:   :nose:
                :zap: 8=:punch: = D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops: :sweat_drops:
             :boot:         :boot:                    :sweat_drops: :sweat_drops: :sweat_drops:"""
        else:
            theguy = """:ok_hand:             :weary:
    :eggplant: :zzz: :necktie: :eggplant:
                    :oil:   :nose:
                :zap: 8=:punch: = D {}
             :trumpet:      :eggplant:                 {} {}
             :boot:         :boot:                    {} {} {}""".format(emo, emo, emo, emo, emo, emo)
        await self.client.say(theguy)

    @commands.command(pass_context=True, aliases=['roll'])
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def dice(self, ctx):
        roll = randint(1, 6)
        dice = ["https://cdn.discordapp.com/attachments/372188609425702915/446370393998229514/dice-1.png",
                "https://cdn.discordapp.com/attachments/372188609425702915/446370398767022090/dice-2.png",
                "https://cdn.discordapp.com/attachments/372188609425702915/446370401510227978/dice-3.png",
                "https://cdn.discordapp.com/attachments/372188609425702915/446370403284156426/dice-4.png",
                "https://cdn.discordapp.com/attachments/372188609425702915/446370404878123019/dice-5.png",
                "https://cdn.discordapp.com/attachments/372188609425702915/446370408610922497/dice-6.png"]
        msg = "It landed on **{}**!".format(roll)
        embed = discord.Embed(description=msg, title="tossed the :game_die:!")
        embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name)
        embed.set_thumbnail(url=dice[roll - 1])
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
        await self.client.send_message(ctx.message.channel, embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def penislength(self, ctx, member: discord.Member=None):
        member = member or ctx.message.author
        inches = randint(2, 12)
        cm = inches * 2.54
        text = "8" + ("=" * inches) + "D" + " " + "\U0001F4A6" * (inches // 2)
        reaction = ""
        if inches >= 9:
            reaction = "\U0001F60D Wow! \U0001F60D"
        elif inches <= 4:
            reaction = "Ehh \U0001F612"
        else:
            reaction = "Nice \U0001F609"
        await self.client.say("{}'s penis is **{} inches!** ({} cm)\n{}\n{}".format(member.mention, inches, cm, text, reaction))

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def compare(self, ctx, member: discord.Member=None):
        inches = randint(2, 12)
        cm = inches * 2.54
        text = "8" + ("=" * inches) + "D" + " " + "{} inches ({} cm)".format(inches, cm)
        userinches = randint(2, 12)
        usercm = userinches * 2.54
        usertext = "8" + ("=" * userinches) + "D" + " " + "{} inches ({} cm)".format(userinches, usercm)

        winmessage = ""
        if inches == userinches:
            winmessage = "Tie!"
        else:
            winner = ctx.message.author if inches > userinches else member
            winmessage = "The winner is {}!".format(winner.mention)
        msg = "{}\n\n{}".format(text, usertext)
        embed = discord.Embed(description=msg)
        embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name)
        embed.set_footer(icon_url=member.avatar_url, text=member.display_name)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/469451848873672704/Eggplant_Emoji_large.png")
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()

        await self.client.send_message(ctx.message.channel, embed=embed, content=winmessage)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def spin(self, ctx, member: discord.Member=None):
        if member:
            member = member
            message = ":regional_indicator_o::regional_indicator_h::warning::regional_indicator_s::regional_indicator_h::regional_indicator_i::regional_indicator_t::exclamation: THIS NI:b::b:A :fire: {} :fire: JUST GOT SPUN ON BY {}! :100: :ok_hand: ".format(member.mention, ctx.message.author.mention)
        else:
            member = ctx.message.author
            message = ":regional_indicator_o::regional_indicator_h::warning::regional_indicator_s::regional_indicator_h::regional_indicator_i::regional_indicator_t::exclamation: THIS NI:b::b:A :fire: {} :fire:JUST SPUN {}! :100: :ok_hand:".format(member.mention, ctx.message.channel.mention)

        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/372188609425702915/436986898641059870/fidget-spinner-gif-transparent-1.gif")
        await self.client.say(content=message, embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def dab(self, ctx, member: discord.Member=None):
        if member:
            member = member
            message = ":regional_indicator_o::regional_indicator_h::warning::regional_indicator_s::regional_indicator_h::regional_indicator_i::regional_indicator_t::exclamation: THIS NI:b::b:A :fire: {} :fire: JUST GOT DABBED ON BY {}! :100: :ok_hand: ".format(member.mention, ctx.message.author.mention)
        else:
            member = ctx.message.author
            message = ":regional_indicator_o::regional_indicator_h::warning::regional_indicator_s::regional_indicator_h::regional_indicator_i::regional_indicator_t::exclamation: THIS NI:b::b:A :fire: {} :fire:JUST DABBED {}! :100: :ok_hand:".format(member.mention, ctx.message.channel.mention)

        f = open("textfiles/dabimages.txt")
        contents = f.readlines()
        link = ""
        rand = randint(0, len(contents))
        counter = 0
        for i in contents:
            if counter == rand:
                link = i
                break
            else:
                counter+=1
        f.close()
        embed = discord.Embed()
        embed.set_image(url=link)
        await self.client.say(content=message, embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def walk(self, ctx, member: discord.Member=None):
        if member:
            member = member
            message = "( ͡° ͜ʖ ͡°) ╯╲___:dog: Don't mind me just taking {} for a walk!".format(member.mention)
        else:
            member = ctx.message.author
            message = "( ͡° ͜ʖ ͡°) ╯╲___ Who wants to go for a walk??"

        await self.client.say(message)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def owo(self, ctx, *, message: str):
        newmsg = message.replace("r", "w").replace("l", "w")
        await self.client.say("**O**w**O** " + newmsg + " **O**w**O**")

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def mock(self, ctx, *, message: str = None):
        channel = ctx.message.channel
        if not message:
            msg = "my name is " + ctx.message.author.mention + " and I don't know how to properly use the mock command"
        else:
            msg = message.lower()
        newmsg = ""
        for c in msg:
            rand = randint(0, 1)
            if rand:
                newmsg = newmsg + c.upper()
            else:
                newmsg = newmsg + c

        embed = discord.Embed(description=newmsg)
        embed.set_thumbnail(url="http://i.imgur.com/upItEiG.jpg")
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
        await self.client.send_message(channel, embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def convert(self, ctx, *, message: str=None):
        if message is None:
            message = "emojipasta bot is the best"
        message = message.lower()
        newmsg = ""
        for c in message:
            if c == " ":
                newmsg = newmsg + ":joy:"
            else:
                newmsg = newmsg + " :regional_indicator_"+c+": "
        await self.client.say(newmsg)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def d(self, ctx):
        d = ["DES", "PA", "CITO"]
        for i in d:
            await self.client.say(i)
            await asyncio.sleep(1)

    def check_duplicate(users):
        di = dict()
        for u in users:
            if not u in di:
                di.update({u: 0})
            else:
                di.update({u: di.get(u) + 1})
        for key, value in di.items():
            if value > 0:
                return True
    @commands.command(pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def brawl(self, ctx, *users):
        if Fun.check_duplicate(users) == True:
            await self.client.say("You cannot duplicate brawlers..")
            return
        brawlers = len(users)
        if brawlers > 5:
            await self.client.say("To prevent this command from filling the chat with spam you are limited to 5 brawlers.")
            return
        elif brawlers == 1:
            await self.client.say("Are you trying to fight yourself..? More than one brawler is required.")
            return
        combatants = list(users)
        attack = ['punched','kicked','slapped','poked','bit']
        bodypart = ['eyes','mouth','arm','leg','stomach','chest','groin','face']
        users = ", ".join(map(str, users))
        await self.client.say("Starting a brawl with {}".format(users))
        await asyncio.sleep(3)
        for i in range (len(combatants)):
            if(len(combatants) == 1):
                await self.client.say("{} is the victor!".format(combatants[0]))
                return
            los = choice(combatants)
            if(len(combatants) == 2):
                vic = choice(combatants)
                if vic == los:
                    combatants.remove(los)
                    vic = combatants[0]
                else:
                    combatants.remove(los)
            elif(brawlers > 2):
                combatants.remove(los)
                vic = choice(combatants)
            atk = choice(attack)
            bpt = choice(bodypart)
            await self.client.say("{0} has {1} {2} in the {3}! {2} is defeated!".format(vic,atk,los,bpt))
            await asyncio.sleep(5)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def flip(self, ctx, *, message: str):
        reverse = message[::-1]
        letters = {' ': ' ','z': 'z','y': 'ʎ','x': 'x','w': 'ʍ','v': 'ʌ','u': 'n','t': 'ʇ','s': 's','r': 'ɹ',
        'q': 'b','p': 'd','o': 'o','n': 'u','m': 'ɯ','l': 'l','k': 'ʞ','j': 'ɾ','i': 'ᴉ','h': 'ɥ',
        'g': 'ƃ','f': 'ɟ','e': 'ǝ','d': 'p','c': 'ɔ','b': 'q','a': 'ɐ'}
        newmsg = ""
        for c in reverse:
            if not letters.get(c):
                continue
            newmsg = newmsg + letters[c]
        await self.client.say(newmsg)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def clap(self, ctx, *, original_clap):
        emojis = [" 👏 "," 👏🏻 "," 👏🏼 "," 👏🏽 "," 👏🏾 "," 👏🏿 "]
        split_clap = original_clap.split()
        new_blocks = []
        for i, block in enumerate(split_clap):
            new_blocks.append(block)
            emoji = choice(emojis)
            new_blocks.append(emoji)
        final_clap = "".join(new_blocks)
        await self.client.say(final_clap)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def pasta(self, ctx, *, original_words):
        generator = EmojipastaGenerator.of_default_mappings()
        final_emoji = generator.generate_emojipasta(original_words)
        await self.client.say(final_emoji)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def unipasta(self, ctx, *, original_words):
        generator = EmojipastaGenerator.of_default_mappings()
        final_emoji = generator.generate_uni_emojipasta(original_words)
        await self.client.say(final_emoji)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def b(self, ctx, *, message: str):
        newmsg = message.replace("b", "\U0001F171").replace("B", "\U0001f171")
        await self.client.say(newmsg)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def jerkit(self, ctx):
        msg = await self.client.say("8:fist:====D")
        await asyncio.sleep(.2)
        await self.client.edit_message(msg,"8=:fist:===D")
        await asyncio.sleep(.3)
        await self.client.edit_message(msg,"8==:fist:==D")
        await asyncio.sleep(.4)
        await self.client.edit_message(msg,"8===:fist:=D")
        await asyncio.sleep(.5)
        await self.client.edit_message(msg,"8====:fist:D")
        await asyncio.sleep(.6)
        await self.client.edit_message(msg,"8===:fist:=D")
        await asyncio.sleep(.5)
        await self.client.edit_message(msg,"8==:fist:==D")
        await asyncio.sleep(.4)
        await self.client.edit_message(msg,"8=:fist:===D")
        await asyncio.sleep(.3)
        await self.client.edit_message(msg,"8:fist:====D")
        await asyncio.sleep(.2)
        await self.client.edit_message(msg,"8:fist:====D:sweat_drops:")

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def ud(self, ctx, *, message: str):
        term = message
        r = requests.get("http://api.urbandictionary.com/v0/define?term=" + term)
        data = json.loads(r.text)
        result = data['result_type']
        if result == "no_results":
            await self.client.say("No definition was found for *" + term + "*")
            return
        definition = data['list'][0]['definition']
        word = data['list'][0]['word']
        example = data['list'][0]['example']
        tu = str(data['list'][0]['thumbs_up'])
        td = str(data['list'][0]['thumbs_down'])
        embed = discord.Embed(title=word, description=definition + "\n\n*" + example + "*")
        embed.set_footer(text="\U0001F44D " + tu + "  |  \U0001F44E " + td)
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
        await self.client.send_message(ctx.message.channel, embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def uw(self, ctx, message: str = None):
        if message == "list":
            await client.say("Here's the master list of links:\nhttps://pastebin.com/FVhnt8xs")
            return
        f = open("textfiles/randomsites.txt");
        contents = f.readlines()
        link = ""
        rand = randint(0, len(contents))
        counter = 0
        for i in contents:
            if counter == rand:
                link = i
                break
            else:
                counter+=1
        f.close()
        embed = discord.Embed(description=link + "\nReport a broken link with the &feedback command.")
        embed.set_author(name=ctx.message.author.display_name + " requested a link!", icon_url=ctx.message.author.avatar_url)
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
        await self.client.send_message(ctx.message.channel, embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def maymay(self, ctx):
        f = open("textfiles/comics.txt")
        contents = f.readlines()
        link = ""
        rand = randint(0, len(contents))
        counter = 0
        for i in contents:
            if counter == rand:
                link = i
                break
            else:
                counter+=1
        f.close()
        embed = discord.Embed()
        embed.set_image(url=link)
        await self.client.say(content="Our :100: devs :ok_hand: enjoy :lion_face::relaxed: them :punch: unironically", embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def bw(self, ctx, message: str = None):
        if message == "list":
            await self.client.say("Here's the master list of links:\nhttps://pastebin.com/dLe1MdPL")
            return
        f = open("textfiles/bannedsites.txt")
        contents = f.readlines()
        link = ""
        rand = randint(0, len(contents))
        counter = 0
        for i in contents:
            if counter == rand:
                link = i
                break
            else:
                counter+=1
        f.close()
        embed = discord.Embed(description=link + "\n:flag_cn: Embrace your non-China privilege by visiting a website banned in China! :flag_cn: \nReport a broken link with the &feedback command.")
        embed.set_author(name=ctx.message.author.display_name + " requested a link!", icon_url=ctx.message.author.avatar_url)
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
        await self.client.send_message(ctx.message.channel, embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def t(self, ctx):
        f = open("textfiles/memetemplates.txt")
        contents = f.readlines()
        link = ""
        rand = randint(0, len(contents))
        counter = 0
        for i in contents:
            if counter == rand:
                link = i
                break
            else:
                counter+=1
        f.close()
        embed = discord.Embed()
        embed.set_image(url=link)
        await self.client.say(content="OK here's the random blank meme template for you!", embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def chan(self, ctx, board: str=None):
        if board is None:
            boards = ['a', 'c', 'f', 'g', 'k', 'm', 'o', 'p', 'v',
                    'vg', 'vr', 'w', 'wg', 'i', 'ic', 'vip', 'qa', 'cm', 'lgbt', '3',
                    'adv', 'an', 'asp', 'biz', 'cgl', 'ck', 'co', 'diy', 'fa', 'fit', 'gd', 'his', 'int',
                    'jp', 'lit', 'mlp', 'mu', 'n', 'news', 'out', 'po', 'qst', 'sci', 'sp', 'tg', 'toy',
                    'trv', 'tv', 'vp', 'wsg', 'wsr', 'x']
            board = boards[randint(0, len(boards) - 1)]
        url = 'https://boards.4chan.org/' + board
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'DNT': '1',
                'Connection': 'keep-alive'}
        r = requests.get(url, headers=headers)
        if not (r.status_code == 200):
            await self.client.say("Invalid board, pls try again!")
            return

        soup = BeautifulSoup(r.content,"html.parser")
        divs = soup.find_all('div', attrs={"class": "thread"})
        yeet = divs[4].find('a', attrs={"class":"fileThumb"})
        despacito = divs[4].find('blockquote', attrs={"class":"postMessage"})
        get_image = yeet.attrs['href']
        get_text = despacito.find_all(text=True)
        thread_id = despacito.attrs['id']
        image = 'https:' + get_image
        text = ''
        if get_text is not None:
            for i in get_text:
                text = text + i
        thread_url = url + '/thread/'
        for a in thread_id:
            if a != 'm':
                thread_url = thread_url + a
        embed = discord.Embed(description=text)
        embed.set_author(name='Click here to view original thread in /' + board + '/', url=thread_url)
        embed.set_image(url=image)
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(Fun(client))
