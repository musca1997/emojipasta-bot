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

class Fun():
    def __init__(self, client):
        self.client = client

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

        dab_images = [
			"https://cdn.discordapp.com/attachments/428960174808498176/436617301249359903/Dab_1.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617300779728908/DAB.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617300779728906/squidward_dab_by_josael281999-dbbuazm.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617300095795211/Woody_dab.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617300095795210/king_dab__clash_royale__by_josael281999-db8mdhl.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617220714528778/3505ebaa-f270-45d4-8693-88574828ef49.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617219707764736/hitler_hits_a_sick_dab_by_alphashitlord-damch71.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617219091333122/fQh7nCY9K1-8.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617219091333121/dab_2.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617218579759124/a79.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617147230453772/Bearded-Dab.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/439001759168462848/giphy.gif",
			"https://cdn.discordapp.com/attachments/428960174808498176/439001759168462849/AS003639_09.gif",
			"https://cdn.discordapp.com/attachments/428960174808498176/439001759860391946/AW386482_01.gif",
			"https://cdn.discordapp.com/attachments/428960174808498176/439001759860391947/dabpuush_by_discopanda_tm-d9znmse.gif",
			"https://cdn.discordapp.com/attachments/428960174808498176/439001760447856640/dab_on_em_rose_by_madithekitten-dasw55o.gif",
			"https://cdn.discordapp.com/attachments/428960174808498176/439256214317170688/20162F022F072F862FBettyWhite.f3633.jpg",
			"https://cdn.discordapp.com/attachments/428960174808498176/439256230528155658/d6d.jpg",
			"https://cdn.discordapp.com/attachments/428960174808498176/439256250312556564/giphy.gif",
			"https://cdn.discordapp.com/attachments/428960174808498176/439256264187445260/hqdefault.jpg",
			"https://cdn.discordapp.com/attachments/428960174808498176/439256283821113344/maxresdefault.jpg",
			"https://cdn.discordapp.com/attachments/428960174808498176/439256300107464715/minion_dab_by_julestheocelot-db7yk05.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617146714292236/248.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617146714292235/249480900001211_1.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617146173358081/1508659373107.gif",
			"https://cdn.discordapp.com/attachments/420589076916207626/436862948200153088/wubba_lubba_dab_dab_by_alexandratale-dbew3ml.png",
            "https://cdn.discordapp.com/attachments/420589076916207626/439972205003145217/92af322e14246ae1291d06fa9e32223a.gif",
            "https://cdn.discordapp.com/attachments/420589076916207626/439972589331283978/tenor.gif",
            "https://cdn.discordapp.com/attachments/420589076916207626/439972589855834115/ee09ebd7068f47c52eff406cf8177c418dbd3e86_hq_by_the8bitdj-dbbdl6e.gif",
            "https://cdn.discordapp.com/attachments/412884243195232257/439972560499769346/dabpuush_by_discopanda_tm-d9znmse.gif",
            "https://cdn.discordapp.com/attachments/420589076916207626/439973096548597761/ovgeujull8bsku3o_by_theophobic-dbk0904.gif",
            "https://cdn.discordapp.com/attachments/420589076916207626/439973217038368784/www_gifcreator_me_dj0utn_by_swap_sans-db6yudf.gif",
            "https://cdn.discordapp.com/attachments/420589076916207626/439973320994324491/harambe.gif",
            "https://cdn.discordapp.com/attachments/420589076916207626/439973445850365972/062717_milcin_arcia_sedar_dab_med_n9garc16.gif",
            "https://cdn.discordapp.com/attachments/420589076916207626/439974137927041044/giphy.gif",
            "https://cdn.discordapp.com/attachments/420589076916207626/439974802183290921/giphy-bdt.gif",
            "https://cdn.discordapp.com/attachments/420589076916207626/439974968537907220/giphy.gif",
            "https://media.discordapp.net/attachments/428960174808498176/443191684981850123/6088d94.png?width=528&height=523",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617144914935829/2e9d4609812ebddeb159f1499e37ec97.png"
		]
        index = randint(0, len(dab_images) - 1)
        embed = discord.Embed()
        embed.set_image(url=dab_images[index])
        await self.client.say(content=message, embed=embed)

        @commands.command(pass_context=True)
        @commands.cooldown(1, 8, commands.BucketType.user)
        async def walk(self, ctx, member: discord.Member=None):
            if member:
                member = member
                message = "( ͡° ͜ʖ ͡°) ╯╲___卐卐卐卐卐 Don't mind me just taking {} for a walk!".format(member.mention)
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
        f = open(os.path.join("textfiles/randomsites.txt"));
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
        f = open(os.path.join("textfiles/comics.txt"))
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
        f = open(os.path.join("textfiles/bannedsites.txt"))
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
        f = open(os.path.join("textfiles/memetemplates.txt"))
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

def setup(client):
    client.add_cog(Fun(client))
