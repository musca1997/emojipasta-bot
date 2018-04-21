from random import choice
from random import randint
import io
import json

from emojigene import EmojipastaGenerator

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import pyqrcode
import png

client = Bot(description="Emojipasta-Bot is a dicord bot for converting text to emojipasta. \n Bot Owner: toiletplunger#8909 \n Congrats! You don't need to add quotes anymore! ", command_prefix="&", pm_help = False)
client.remove_command("help")

class Bot_Info:

    @client.command()
    async def orange(*args):
        await client.say("<@294963984535257089> is my best big titty goth gf <33333")

    @client.command()
    async def ping(*args):

    	await client.say(":ping_pong: Pong!")
    	await asyncio.sleep(1)
    	await client.say(":warning: I'M GAY")

    @client.command(pass_context = True)
    async def feedback(ctx, *, user_feedback):
        await client.say("K, already sent your feedback 😎💯 ")
        await client.send_message(discord.Object(id='434726800711483393'), str(ctx.message.author) + ' from <' + str(ctx.message.server) + '> just sent a feedback: ```' + str(user_feedback) + '```')


    @client.command()
    async def help(*args):
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
        embed.add_field(name="**&mock**", value="Use &mock with text to gEt cOoL tExT.")
        embed.add_field(name="**&jerkit**", value="Use &jerkit to jerk off when you can't jerk off.")
        embed.add_field(name="**&walk**", value="Use &walk @someone to walk with them!")
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

class Bot_Function:
    @client.command(pass_context=True)
    async def pasta(ctx, *, original_words):
        generator = EmojipastaGenerator.of_default_mappings()
        final_emoji = generator.generate_emojipasta(original_words)

        await client.say(final_emoji)
        await client.send_message(discord.Object(id="436544688745480203"), "```&pasta called from <" + str(ctx.message.server) + ">```")

    @client.command(pass_context=True)
    async def yn(ctx, *args):
        decide_list = ['YES!','NO!']
        decide_answer = choice(decide_list)
        await client.say(decide_answer)
        await client.send_message(discord.Object(id="436544688745480203"), "```&yn invoked from <" + str(ctx.message.server) + ">```")

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
        await client.send_message(discord.Object(id="436544688745480203"), "```&clap invoked from <" + str(ctx.message.server) + ">```")

    @client.command(pass_context=True)
    async def rn(ctx, arg1=1, arg2=100):
        try:
            random_number = randint(arg1, arg2)
            await client.say("{}-{}: {}".format(arg1, arg2, random_number))
            await client.send_message(discord.Object(id="436544688745480203"), "```&rn invoked from <" + str(ctx.message.server) + ">```")
        except ValueError:
            await client.say("Invalid range")

    @client.command(pass_context=True)
    async def b(ctx, *, message: str):
        newmsg = message.replace("b", "\U0001F171").replace("B", "\U0001f171")
        await client.say(newmsg)
        await client.send_message(discord.Object(id="436544688745480203"), "```&b invoked from <" + str(ctx.message.server) + ">```")

    @client.command(pass_context=True)
    async def penislength(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        inches = randint(2, 12)
        cm = inches * 2.54
        str = "8" + ("=" * inches) + "D" + " " + "\U0001F4A6" * (inches // 2)

        await client.say("{}'s penis is **{} inches!** ({} cm)\n{}".format(member.mention, inches, cm, str))
        await client.send_message(discord.Object(id="436544688745480203"), "```&penislength invoked from <" + str(ctx.message.server) + ">```")
        if inches >= 9:
            await client.say("\U0001F60D Wow! \U0001F60D")
        elif inches <= 4:
            await client.say("Ehh \U0001F612")
        else:
            await client.say("Nice \U0001F609")

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
			"https://cdn.discordapp.com/attachments/428960174808498176/436617146714292236/248.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617146714292235/249480900001211_1.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617146173358081/1508659373107.gif",
            "https://cdn.discordapp.com/attachments/420589076916207626/436862948200153088/wubba_lubba_dab_dab_by_alexandratale-dbew3ml.png",
			"https://cdn.discordapp.com/attachments/428960174808498176/436617144914935829/2e9d4609812ebddeb159f1499e37ec97.png"
		]
        index = randint(0, len(dab_images) - 1)
        await client.say(dab_images[index] + "\n" + message)
        await client.send_message(discord.Object(id="436544688745480203"), "```&dab invoked from <" + str(ctx.message.server) + ">```")

    @client.command(pass_context=True)
    async def walk(ctx, member: discord.Member=None):
        if member:
            member = member
            message = "( ͡° ͜ʖ ͡°) ╯╲___卐卐卐卐卐 Don't mind me just taking {} for a walk!".format(member.mention)
        else:
            member = ctx.message.author
            message = "( ͡° ͜ʖ ͡°) ╯╲___ Who wants to go for a walk??"

        await client.say(message)
        await client.send_message(discord.Object(id="436544688745480203"), "```&walk invoked from <" + str(ctx.message.server) + ">```")


    @client.command(pass_context=True)
    async def jerkit(ctx):
        await client.send_message(discord.Object(id="436544688745480203"), "```&jerkit invoked from <" + str(ctx.message.server) + ">```")
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

    @client.command()
    async def owo(*, message: str):
        newmsg = message.replace("r", "w").replace("l", "w")
        await client.say("**O**w**O** " + newmsg + " **O**w**O**")

    @client.command()
    async def mock(*, message: str):
        msg = message.lower()
        newmsg = ""
        for c in msg:
            rand = randint(0, 1)
            if rand:
                newmsg = newmsg + c.upper()
            else:
                newmsg = newmsg + c

        await client.say("https://cdn.discordapp.com/attachments/420589076916207626/437090583861788687/spongebob.png \n" + newmsg)


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
    	return await client.change_presence(game=discord.Game(name='&help | DADDYS PLUNGER'))

    client.run('')

if __name__ == "__main__":
    main()
