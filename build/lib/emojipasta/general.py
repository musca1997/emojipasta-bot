from random import choice
from random import randint
import discord
import asyncio
import pyqrcode
import png
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class General():
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def poll(self, ctx, *, input: str):
        tokens = input.split(",")
        question = tokens[0]
        options = tokens[1:]
        optioncount = len(options)
        if optioncount == 1:
            await self.client.say("It's not really a poll if there's only one option.")
            return
        if optioncount > 10:
            await self.client.say("Poll option limit is 10! Try simplifying your question.")
            return
        reactions = ['😝', '😎', '😁', '😍', '😂', '😚', '😮', '😇', '🤗', '😌']
        msg = ""
        for x, option in enumerate(options):
            msg = msg + "\n{} {}".format(reactions[x], option)

        embed = discord.Embed(title=question, description=msg, colour=0xffcc4d)
        embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name + " asks,")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/446747780157931542/thinking.png")
        message = await self.client.say(embed=embed)

        for reaction in reactions[:optioncount]:
            await self.client.add_reaction(message, reaction)

        await self.client.edit_message(message, embed=embed)

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def ynpoll(self, ctx, *, input: str=None):
        footer = ""
        if input is None:
            footer = "You can ask your own question too! &ynpoll <question>"
            input = "Is Emojipasta Bot the best Discord bot?"
        msg = "😁 Yes\n😠 No"
        embed = discord.Embed(title=input, description=msg, colour=0xffcc4d)
        embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name + " asks,")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/446747780157931542/thinking.png")
        if footer is not "":
            embed.set_footer(text=footer)

        message = await self.client.say(embed=embed)
        await self.client.add_reaction(message, '😁')
        await self.client.add_reaction(message, '😠')

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def yn(self, ctx, *args):
        decide_list = [':heavy_check_mark: YES!',':heavy_multiplication_x: NO!']
        decide_answer = choice(decide_list)
        await self.client.say(decide_answer)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def rn(self, ctx, arg1=1, arg2=100):
        try:
            random_number = randint(arg1, arg2)
            await self.client.say("{}-{}: {}".format(arg1, arg2, random_number))
        except ValueError:
            await self.client.say("Invalid range")

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def qr(self, ctx, *, msg):
        qr = pyqrcode.create(msg)
        qr.png('qrcode.png', scale=5)
        await self.client.send_file(ctx.message.channel, 'qrcode.png')

def setup(client):
    client.add_cog(General(client))
