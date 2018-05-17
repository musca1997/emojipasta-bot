from random import randint
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Games():
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def rps(self, ctx, choice: str=None):
        rps = ["rock", "paper", "scissors"]
        if choice is None:
            choice = rps[randint(0, 2)]
        if choice not in rps:
            await self.client.say("Syntax: &rps rock|paper|scissors")
            return
        emoji = ["\U0001F44A", "\U0001F91A", "\U0000270C"]
        num = randint(0, 2)

        index = rps.index(choice)
        result = ["Tie!", "Emojipasta Bot wins!", "{} wins!"]
        resultnum = (num - index) % 3

        msg = "{}\n\n{}\n\n{}".format(emoji[index], result[resultnum].format(ctx.message.author.display_name), emoji[num])
        botuser = ctx.message.server.get_member("407372430835843084")
        embed = discord.Embed(description=msg, colour=0xffcc4d)
        embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name)
        embed.set_footer(icon_url=botuser.avatar_url, text=botuser.display_name)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/446780280490164235/collision.png")
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(Games(client))
