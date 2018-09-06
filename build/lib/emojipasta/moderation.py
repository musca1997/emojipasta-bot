import discord
from discord.ext import commands

class Moderation:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def ban(self, ctx, target: discord.User, *reason):
        try:
            if (ctx.message.author.server_permissions.ban_members == True):
                await self.client.ban(target)
                reason = " ".join(map(str, reason))
                await self.client.say("Banned {0} {1}".format(target, reason))
            else:
                await self.client.say("You don't have the required permissions, {}".format(ctx.message.author))
        except Exception as e:
            await self.client.say("Failed. My role is not higher than that person.")

    @commands.command(pass_context=True)
    async def kick(self, ctx, target: discord.User, *reason):
        try:
            if (ctx.message.author.server_permissions.ban_members == True):
                await self.client.kick(target)
                reason = " ".join(map(str, reason))
                await self.client.say("Kicked {0} {1}".format(target, reason))
            else:
                await self.client.say("You don't have the required permissions, {}".format(ctx.message.author))
        except Exception as e:
            await self.client.say("Failed. My role is not higher than that person.")

    @commands.command(pass_context=True)
    async def nick(self, ctx, target: discord.User, *, nickname):
        try:
            if (ctx.message.author.server_permissions.manage_nicknames == True):
                await self.client.change_nickname(target, nickname)
                await self.client.say("Done.")

            elif (ctx.message.author.server_permissions.change_nickname == True) and (target == '<@' + ctx.message.author.id + '>'):
                await self.client.change_nickname(target, nickname)
                await self.client.say("Done.")
            else:
                await self.client.say("You don't have the required permissions, {}".format(ctx.message.author))
        except Exception as e:
            await self.client.say("Failed. My role is not higher than that person.")

def setup(client):
    client.add_cog(Moderation(client))
