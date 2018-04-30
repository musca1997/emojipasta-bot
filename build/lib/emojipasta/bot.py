from random import choice
from random import randint
import io
import json

from emojigene import EmojipastaGenerator

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import platform
import pyqrcode
import png

client = Bot(description="Emojipasta-Bot is a dicord bot for converting text to emojipasta. \n Bot Owner: toiletplunger#8909 \n Congrats! You don't need to add quotes anymore! ", command_prefix="&", pm_help = False)
client.remove_command("help")

class Bot_Info:

    @client.command(pass_context=True)
    async def orange(ctx, *args):
        await client.say("<@294963984535257089> is my best big titty goth gf <33333")
        await client.send_message(discord.Object(id="436544688745480203"), "```&orange invoked from <" + str(ctx.message.server) + ">```")

    @client.command(pass_context=True)
    async def ping(*args):

    	await client.say(":ping_pong: Pong!")
    	await asyncio.sleep(1)
    	await client.say(":warning: I'M GAY")

    @client.command(pass_context = True)
    async def feedback(ctx, *, user_feedback):
        await client.say("K, already sent your feedback 😎💯 ")
        await client.send_message(discord.Object(id='434726800711483393'), str(ctx.message.author) + ' from <' + str(ctx.message.server) + '> just sent a feedback: ```' + str(user_feedback) + '```')

    @client.command(pass_context=True)
    async def help(ctx, *args):
        embed = discord.Embed(title="Kermit Klan House", colour=discord.Colour(0xa4302c), url="https://discord.gg/JHNRwr6", description="Emojipasta-Bot is a bot mainly for converting text to emojipasta.")

        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/419521490220744705/429667256717279262/f42b7e7.png")
        embed.set_author(name="Emojipasta-Bot Info", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/attachments/419521490220744705/429667256717279262/f42b7e7.png")
        embed.set_footer(text="Powered by Kermit Klan House", icon_url="https://cdn.discordapp.com/attachments/419521490220744705/429667256717279262/f42b7e7.png")

        embed.add_field(name="**&pasta**", value="Use &pasta to convert text to emojipasta.\nInput:```&pasta This is a shitty bot\n```Output:\n```This 😤 is a shitty 💩💩 bot```")
        embed.add_field(name="**&clap**", value="Use &clap to add clap emoji to text.\nInput:```&clap Mommy bought me new pony toy I love you mama\n```Output:\n```Mommy 👏🏻 bought 👏🏼 me 👏 new 👏🏽 pony 👏🏿 toy 👏🏾 I 👏 love 👏🏾 you 👏🏽 mama```")
        embed.add_field(name="**&yn**", value="Use &yn to make decision (yes or no).\nInput:```&yn Should I use this function?\n```Output:\n```YES!```")
        embed.add_field(name="**&rn**", value="Use &rn to generate a random number.\nInput (Default Range):```&rn\n```Output:\n```1-100: <number>\n```Input (Custom Range):```&rn 87 305\n```Output:\n```87-305: <number>```")
        embed.add_field(name="**&b**", value="Use &b to replace any letter 'b' with 🅱️.\nInput:```&b Emojipasta bot is the best bot!\n```Output:\n```Emojipasta 🅱️ot is the 🅱️est 🅱️ot!```")
        embed.add_field(name="**&owo**", value="Use &owo with text to make you owo!")
        embed.add_field(name="**&qr**", value="Use &qr with text to generate your own qrcode!")
        embed.add_field(name="**&penislength**", value="Use &penislength to measure your penis length! Try tagging someone to find out theirs!")
        embed.add_field(name="**&dab**", value="Use &dab @someone to dab on them!")
        embed.add_field(name="**&spin**", value="Use &spin @someone to spin on them!")
        embed.add_field(name="**&mock**", value="Use &mock with text to gEt cOoL tExT.")
        embed.add_field(name="**&userinfo**", value="Use &userinfo or &serverinfo to get the information.")
        embed.add_field(name="**&jerkit**", value="Use &jerkit to jerk off when you can't jerk off. You can only use it once every 5min.")
        embed.add_field(name="**&walk**", value="Use &walk @someone to walk with them!")
        embed.add_field(name="**&brawl**", value="Use &brawl @someone @someone to let them fight!")
        embed.add_field(name="**&ban/&kick/&nick**", value="Only higher roles of the server can use these functions.")
        embed.add_field(name="**&ping**", value="Nothing special. Just to test if bot is working.")
        embed.add_field(name="**&feedback**", value="Use this to send feedback, we'll contact you if your feedback is valuable.")
        embed.add_field(name="**&help**", value="Nothing special. Just to get this info and help message.")
        embed.add_field(name="💬", value=str(len(client.servers))+ ' **servers**', inline=True)
        embed.add_field(name="🏠", value=str(len(set(client.get_all_members())))+ ' **users**', inline=True)
        embed.add_field(name="👁", value="[support](https://discord.gg/JHNRwr6)", inline=True)
        embed.add_field(name="💦", value="[github](https://github.com/musca1997/emojipasta-bot)", inline=True)
        embed.add_field(name="💯", value="[vote](https://discordbots.org/bot/429662497172357123)", inline=True)
        embed.add_field(name="😎", value="[invite](https://discordapp.com/oauth2/authorize?client_id=429662497172357123&scope=bot&permissions=8)", inline=True)

        await client.say(content="So here's the info of Emojipasta-Bot ", embed=embed)
        await Bot_Function.log("help", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def userinfo(ctx, *, user: discord.Member=None):
        """Shows users's informations"""
        author = ctx.message.author
        server = ctx.message.server

        if not user:
            user = author

        roles = [x.name for x in user.roles if x.name != "@everyone"]

        joined_at = user.joined_at
        since_created = (ctx.message.timestamp - user.created_at).days
        since_joined = (ctx.message.timestamp - joined_at).days
        user_joined = joined_at.strftime("%d %b %Y %H:%M")
        user_created = user.created_at.strftime("%d %b %Y %H:%M")
        member_number = sorted(server.members,
                                  key=lambda m: m.joined_at).index(user) + 1

        created_on = "{}\n({} days ago)".format(user_created, since_created)
        joined_on = "{}\n({} days ago)".format(user_joined, since_joined)

        game = "Chilling in {} status".format(user.status)

        if user.game is None:
            pass
        elif user.game.url is None:
            game = "Playing {}".format(user.game)
        else:
            game = "Streaming: [{}]({})".format(user.game, user.game.url)

        if roles:
            roles = sorted(roles, key=[x.name for x in server.role_hierarchy
                                           if x.name != "@everyone"].index)
            roles = ", ".join(roles)
        else:
            roles = "None"

        data = discord.Embed(description=game, colour=user.colour)
        data.add_field(name="Joined Discord on", value=created_on)
        data.add_field(name="Joined this server on", value=joined_on)
        data.add_field(name="Roles", value=roles, inline=False)
        data.set_footer(text="Member #{} | User ID:{}"
                                "".format(member_number, user.id))

        name = str(user)
        name = " ~ ".join((name, user.nick)) if user.nick else name

        if user.avatar_url:
            data.set_author(name=name, url=user.avatar_url)
            data.set_thumbnail(url=user.avatar_url)
        else:
            data.set_author(name=name)

        try:
            await client.say(embed=data)
            await client.send_message(discord.Object(id="436544688745480203"), "```&userinfo invoked from <" + str(ctx.message.server) + ">```")
        except discord.HTTPException:
            await client.say("I need the `Embed links` permission "
                                   "to send this")

    @client.command(pass_context=True)
    async def serverinfo(ctx):
        """Shows server's informations"""
        server = ctx.message.server
        online = len([m.status for m in server.members
                         if m.status == discord.Status.online or
                         m.status == discord.Status.idle])
        total_users = len(server.members)
        text_channels = len([x for x in server.channels
                             if x.type == discord.ChannelType.text])
        voice_channels = len([x for x in server.channels
                                if x.type == discord.ChannelType.voice])
        passed = (ctx.message.timestamp - server.created_at).days
        created_at = ("Since {}. That's over {} days ago!"
                         "".format(server.created_at.strftime("%d %b %Y %H:%M"),
                                    passed))

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(
            description=created_at,
            colour=discord.Colour(value=colour))
        data.add_field(name="Region", value=str(server.region))
        data.add_field(name="Users", value="{}/{}".format(online, total_users))
        data.add_field(name="Text Channels", value=text_channels)
        data.add_field(name="Voice Channels", value=voice_channels)
        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="Owner", value=str(server.owner))
        data.set_footer(text="Server ID: " + server.id)

        if server.icon_url:
            data.set_author(name=server.name, url=server.icon_url)
            data.set_thumbnail(url=server.icon_url)
        else:
            data.set_author(name=server.name)

        try:
            await client.say(embed=data)
            await client.send_message(discord.Object(id="436544688745480203"), "```&serverinfo invoked from <" + str(ctx.message.server) + ">```")
        except discord.HTTPException:
            await client.say("I need the `Embed links` permission "
                                  "to send this")

class Bot_Function:

    async def log(command, server, time):
        embed = discord.Embed(description="used the " + command + " command.", timestamp=time)
        embed.set_author(name=server)
        await client.send_message(discord.Object(id="436544688745480203"), embed=embed)

    @client.command(pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def brawl(ctx, *users):
        await Bot_Function.log("brawl", ctx.message.server, ctx.message.timestamp)
        brawlers = len(users)
        if brawlers > 5:
            await client.say("To prevent this command from filling the chat with spam you are limited to 5 brawlers.")
            return
        elif brawlers == 1:
            await client.say("Are you trying to fight yourself..? More than one brawler is required.")
            return
        combatants = list(users)
        attack = ['punched','kicked','slapped','poked','bit']
        bodypart = ['eyes','mouth','arm','leg','stomach','chest','groin','face']
        users = ", ".join(map(str, users))
        await client.say("Starting a brawl with {}".format(users))
        await asyncio.sleep(3)
        for i in range (len(combatants)):
            if(len(combatants) == 1):
                await client.say("{} is the victor!".format(combatants[0]))
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
            await client.say("{0} has {1} {2} in the {3}! {2} is defeated!".format(vic,atk,los,bpt))
            await asyncio.sleep(5)

    @client.command(pass_context=True)
    async def pasta(ctx, *, original_words):
        generator = EmojipastaGenerator.of_default_mappings()
        final_emoji = generator.generate_emojipasta(original_words)

        await client.say(final_emoji)
        await Bot_Function.log("pasta", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def yn(ctx, *args):
        decide_list = ['YES!','NO!']
        decide_answer = choice(decide_list)
        await client.say(decide_answer)
        await Bot_Function.log("yn", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def clap(ctx, *, original_clap):
        emojis = [" 👏 "," 👏🏻 "," 👏🏼 "," 👏🏽 "," 👏🏾 "," 👏🏿 "]
        split_clap = original_clap.split()
        new_blocks = []
        for i, block in enumerate(split_clap):
            new_blocks.append(block)
            emoji = choice(emojis)
            new_blocks.append(emoji)
        final_clap = "".join(new_blocks)
        await client.say(final_clap)
        await Bot_Function.log("clap", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def rn(ctx, arg1=1, arg2=100):
        try:
            random_number = randint(arg1, arg2)
            await client.say("{}-{}: {}".format(arg1, arg2, random_number))
            await Bot_Function.log("rn", ctx.message.server, ctx.message.timestamp)
        except ValueError:
            await client.say("Invalid range")

    @client.command(pass_context=True)
    async def b(ctx, *, message: str):
        newmsg = message.replace("b", "\U0001F171").replace("B", "\U0001f171")
        await client.say(newmsg)
        await Bot_Function.log("b", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def penislength(ctx, member: discord.Member=None):
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
        await client.say("{}'s penis is **{} inches!** ({} cm)\n{}\n{}".format(member.mention, inches, cm, text, reaction))
        await Bot_Function.log("penislength", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def spin(ctx, member: discord.Member=None):
        if member:
            member = member
            message = ":regional_indicator_o::regional_indicator_h::warning::regional_indicator_s::regional_indicator_h::regional_indicator_i::regional_indicator_t::exclamation: THIS NI:b::b:A :fire: {} :fire: JUST GOT SPUN ON BY {}! :100: :ok_hand: ".format(member.mention, ctx.message.author.mention)
        else:
            member = ctx.message.author
            message = ":regional_indicator_o::regional_indicator_h::warning::regional_indicator_s::regional_indicator_h::regional_indicator_i::regional_indicator_t::exclamation: THIS NI:b::b:A :fire: {} :fire:JUST SPUN {}! :100: :ok_hand:".format(member.mention, ctx.message.channel.mention)

        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/372188609425702915/436986898641059870/fidget-spinner-gif-transparent-1.gif")
        await client.say(content=message, embed=embed)
        await Bot_Function.log("spin", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def dab(ctx, member: discord.Member=None):
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
			"https://cdn.discordapp.com/attachments/428960174808498176/436617144914935829/2e9d4609812ebddeb159f1499e37ec97.png"
		]
        index = randint(0, len(dab_images) - 1)
        embed = discord.Embed()
        embed.set_image(url=dab_images[index])
        await client.say(content=message, embed=embed)
        await Bot_Function.log("dab", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def walk(ctx, member: discord.Member=None):
        if member:
            member = member
            message = "( ͡° ͜ʖ ͡°) ╯╲___卐卐卐卐卐 Don't mind me just taking {} for a walk!".format(member.mention)
        else:
            member = ctx.message.author
            message = "( ͡° ͜ʖ ͡°) ╯╲___ Who wants to go for a walk??"

        await client.say(message)
        await Bot_Function.log("walk", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def jerkit(ctx):
        await Bot_Function.log("jerkit", ctx.message.server, ctx.message.timestamp)
        msg = await client.say("8:fist:====D")
        await asyncio.sleep(.2)
        await client.edit_message(msg,"8=:fist:===D")
        await asyncio.sleep(.3)
        await client.edit_message(msg,"8==:fist:==D")
        await asyncio.sleep(.4)
        await client.edit_message(msg,"8===:fist:=D")
        await asyncio.sleep(.5)
        await client.edit_message(msg,"8====:fist:D")
        await asyncio.sleep(.6)
        await client.edit_message(msg,"8===:fist:=D")
        await asyncio.sleep(.5)
        await client.edit_message(msg,"8==:fist:==D")
        await asyncio.sleep(.4)
        await client.edit_message(msg,"8=:fist:===D")
        await asyncio.sleep(.3)
        await client.edit_message(msg,"8:fist:====D")
        await asyncio.sleep(.2)
        await client.edit_message(msg,"8:fist:====D:sweat_drops:")

    @client.command(pass_context=True)
    async def qr(ctx, *, msg):
        qr = pyqrcode.create(msg)
        qr.png('qrcode.png', scale=5)
        await client.send_file(ctx.message.channel, 'qrcode.png')
        await Bot_Function.log("qr", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def owo(ctx, *, message: str):
        newmsg = message.replace("r", "w").replace("l", "w")
        await client.say("**O**w**O** " + newmsg + " **O**w**O**")
        await Bot_Function.log("owo", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def mock(ctx, *, message: str = None):
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
        await client.send_message(channel, embed=embed)
        await Bot_Function.log("mock", ctx.message.server, ctx.message.timestamp)

    @client.command(pass_context=True)
    async def ban(ctx, target: discord.User, *reason):
        try:
            if (ctx.message.author.server_permissions.ban_members == True):
                await client.ban(target)
                reason = " ".join(map(str, reason))
                await client.say("Banned {0} {1}".format(target, reason))
            else:
                await client.say("You don't have the required permissions, {}".format(ctx.message.author))
        except Exception as e:
            await client.say("Failed. My role is not higher than that person.")

    @client.command(pass_context=True)
    async def kick(ctx, target: discord.User, *reason):
        try:
            if (ctx.message.author.server_permissions.ban_members == True):
                await client.kick(target)
                reason = " ".join(map(str, reason))
                await client.say("Kicked {0} {1}".format(target, reason))
            else:
                await client.say("You don't have the required permissions, {}".format(ctx.message.author))
        except Exception as e:
            await client.say("Failed. My role is not higher than that person.")

    @client.command(pass_context=True)
    async def nick(ctx, target: discord.User, *, nickname):
        try:
            if (ctx.message.author.server_permissions.ban_members == True):
                await client.change_nickname(target, nickname)
                await client.say("Done.")
            else:
                await client.say("You don't have the required permissions, {}".format(ctx.message.author))
        except Exception as e:
            await client.say("Failed. My role is not higher than that person.")

    @client.command(pass_context=True)
    async def status(ctx,  *, new_stat):
        new_stat = "&help | " + new_stat
        if (str(ctx.message.author) == "toiletplunger#8909" or str(ctx.message.author)  == "SpicyBigDaddy#8008" or str(ctx.message.author)  == "Frankup#0001" or str(ctx.message.author)  == "Orange#6303"):
            await client.change_presence(game=discord.Game(name=(new_stat)))
            await client.say("Done.")
        else:
            await client.say("HAHA CUCKED U DONT HAVE THE PERMISSION TO CHANGE MY STATUS.")

    @client.command(pass_context=True)
    async def shrek(ctx):
        channel = ctx.message.channel
        author = ctx.message.author
        message = author.mention + " has invited Shrek to visit " + channel.mention + "!"
        embed = discord.Embed(description=message)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/421005964276138005/434538229438349313/Shrek_emoji.png")
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
        await client.send_message(channel, embed=embed)
        await Bot_Function.log("shrek", ctx.message.server, ctx.message.timestamp)


def main():
    @client.event
    async def on_ready():
    	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    	print('--------')
    	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    	print('--------')
    	print('Use this link to invite {}:'.format(client.user.name))
    	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    	print('--------')
    	print('--------')

    client.run('')

if __name__ == "__main__":
    main()
