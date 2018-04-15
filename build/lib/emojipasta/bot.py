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
        embed.add_field(name="**&ping**", value="Nothing special. Just to test if bot is working.")
        embed.add_field(name="**&help**", value="Nothing special. Just to get this info and help message.")
        embed.add_field(name="💬", value=str(len(client.servers))+ ' **servers**', inline=True)
        embed.add_field(name="🏠", value=str(len(set(client.get_all_members())))+ ' **users**', inline=True)
        embed.add_field(name="👁", value="[support](https://discord.gg/JHNRwr6)", inline=True)
        embed.add_field(name="💦", value="[github](https://github.com/musca1997/emojipasta-bot)", inline=True)
        embed.add_field(name="💯", value="[vote](https://discordbots.org/bot/429662497172357123)", inline=True)
        embed.add_field(name="😎", value="[invite](https://discordapp.com/oauth2/authorize?client_id=429662497172357123&scope=bot&permissions=8)", inline=True)

        await client.say(content="So here's the info of Emojipasta-Bot ", embed=embed)

class Bot_Function:
    @client.command()
    async def pasta(*, original_words):
        generator = EmojipastaGenerator.of_default_mappings()
        final_emoji = generator.generate_emojipasta(original_words)

        await client.say(final_emoji)

    @client.command()
    async def yn(*args):
        decide_list = ['YES!','NO!']
        decide_answer = choice(decide_list)
        await client.say(decide_answer)

    @client.command()
    async def clap(*, original_clap):
        emojis = [" 👏 "," 👏🏻 "," 👏🏼 "," 👏🏽 "," 👏🏾 "," 👏🏿 "]
        split_clap = original_clap.split()
        new_blocks = []
        for i, block in enumerate(split_clap):
            new_blocks.append(block)
            emoji = choice(emojis)
            new_blocks.append(emoji)
        final_clap = "".join(new_blocks)
        await client.say(final_clap)
       
    @client.command()
    async def rn(arg1=1, arg2=100):
        try:
            random_number = randint(arg1, arg2)
            await client.say("{}-{}: {}".format(arg1, arg2, random_number))
        except ValueError:
            await client.say("Invalid range")


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
