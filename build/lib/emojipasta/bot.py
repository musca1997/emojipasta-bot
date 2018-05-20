from random import choice
from random import randint
import io
import os

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import platform
from util.keys import DISCORD_BOT_KEY

client = Bot(description="Emojipasta-Bot is a dicord bot for converting text to emojipasta. \n Bot Owner: toiletplunger#8909 \n Congrats! You don't need to add quotes anymore! ", command_prefix="&", pm_help = False)
client.remove_command("help")

class Bot_Events:

    @client.event
    async def on_command_error(error, ctx):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(description=str(error))
            embed.set_author(name=ctx.message.author)
            embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
            await client.send_message(ctx.message.channel, embed=embed)
    @client.event
    async def on_command(command, ctx):
        logembed = discord.Embed(description="used the " + str(command) + " command.", timestamp=ctx.message.timestamp)
        logembed.set_author(name=ctx.message.server)
        await client.send_message(discord.Object(id="436544688745480203"), embed=logembed)

    @client.event
    async def on_member_join(member):
        server = member.server
        if not (server.id == "419521489759502337"):
            return
        message = "Hello, welcome to Kermit House of Shitposting <@" + member.id + ">! Home of the Emojipasta Bot. We are looking for Python developers. If you are interested, please check <#444895389921837067> :) If not, chill with us and use the bot!!!"
        await client.send_message(discord.Object(id="420586176467042316"), content=message)
    @client.event
    async def on_member_remove(member):
        server = member.server
        if not (server.id == "419521489759502337"):
            return
        message = "The faggot known as <@" + member.id + "> has left :( \nhttps://cdn.discordapp.com/attachments/446345808346873858/446673433602818048/20180517_100014.png"
        await client.send_message(discord.Object(id="420586176467042316"), content=message)

    @client.event
    async def on_server_join(server):
        server = server
        online = len([m.status for m in server.members if m.status == discord.Status.online or m.status == discord.Status.idle])
        total_users = len(server.members)
        text_channels = len([x for x in server.channels if x.type == discord.ChannelType.text])
        voice_channels = len([x for x in server.channels if x.type == discord.ChannelType.voice])

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(description="", colour=discord.Colour(value=colour))
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
            await client.send_message(discord.Object(id="436544688745480203"), content="I just got **added** into a new server! Now I'm in " + str(len(client.servers)) + " servers with " + str(len(set(client.get_all_members()))) + " users.", embed=data)
        except discord.HTTPException:
            await client.say("I need the `Embed links` permission to send this")

    @client.event
    async def on_server_remove(server):
        server = server
        online = len([m.status for m in server.members if m.status == discord.Status.online or m.status == discord.Status.idle])
        total_users = len(server.members)
        text_channels = len([x for x in server.channels if x.type == discord.ChannelType.text])
        voice_channels = len([x for x in server.channels if x.type == discord.ChannelType.voice])

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(description="", colour=discord.Colour(value=colour))
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
            await client.send_message(discord.Object(id="436544688745480203"), content="I just got **removed** from this server. Press XD to pay respect. Now I'm in " + str(len(client.servers)) + " servers with " + str(len(set(client.get_all_members()))) + " users.", embed=data)
        except discord.HTTPException:
            await client.say("I need the `Embed links` permission to send this")

class Bot_Info:

    @client.command(pass_context=True, aliases=['users', 'servers'])
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def count(ctx, *args):
        embed = discord.Embed(description="\n**So here is the server and user count.**")
        embed.add_field(name="💬", value=str(len(client.servers))+ ' **servers**', inline=True)
        embed.add_field(name="🏠", value=str(len(set(client.get_all_members())))+ ' **users**', inline=True)
        await client.say(embed=embed)

    @client.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def help(ctx, *args):
        await client.say("Check out command list here: https://www.emojipasta.fun/commands/ \nJoin our support server if you need more info: https://discord.gg/JHNRwr6")

    @client.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def invite(ctx, *args):
        await client.say("https://discordapp.com/oauth2/authorize?client_id=429662497172357123&scope=bot&permissions=8")

    @client.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def vote(ctx, *args):
        await client.say("https://discordbots.org/bot/429662497172357123")

    @client.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def orange(ctx, *args):
        await client.say("@Orange is my best big titty goth gf <33333")

    @client.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def github(ctx, *args):
        await client.say("https://github.com/musca1997/emojipasta-bot")

    @client.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def ping(ctx, *args):
        await client.say(":ping_pong: Pong!")
        await asyncio.sleep(1)
        await client.say(":warning: I'M GAY")

    @commands.cooldown(1, 30, commands.BucketType.user)
    @client.command(pass_context = True)
    async def feedback(ctx, *, user_feedback):
        await client.say("K, already sent your feedback 😎💯 ")
        await client.send_message(discord.Object(id='434726800711483393'), str(ctx.message.author) + ' from <' + str(ctx.message.server) + '> just sent a feedback: ```' + str(user_feedback) + '```')

    @client.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
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
        except discord.HTTPException:
            await client.say("I need the `Embed links` permission "
                                   "to send this")

    @client.command(pass_context=True)
    @commands.cooldown(1, 8, commands.BucketType.user)
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
        except discord.HTTPException:
            await client.say("I need the `Embed links` permission "
                                  "to send this")

class Restricted:

    @client.command(pass_context=True)
    async def status(ctx,  *, new_stat):
        new_stat = "&help | " + new_stat
        if (str(ctx.message.author.id) == "349838216637186048" or str(ctx.message.author.id)  == "396783619466854402" or str(ctx.message.author.id)  == "183457916114698241" or str(ctx.message.author.id)  == "294963984535257089"):
            await client.change_presence(game=discord.Game(name=(new_stat)))
            await client.say("Done.")
        else:
            await client.say("HAHA CUCKED U DONT HAVE THE PERMISSION TO CHANGE MY STATUS.")

    @client.event
    async def on_message(message):
        await client.process_commands(message)
        if not (message.channel.id == "431202784575094794" or message.channel.id == "442488016523624448"):
            return
        if message.attachments:
            url = str(message.attachments[0]['url'])
        if message.embeds:
            url = str(message.embeds[0]['url'])
        else:
            return

        files = {"431202784575094794": "textfiles/memetemplates.txt", "442488016523624448": "textfiles/comics.txt"}
        f = open(files[str(message.channel.id)], 'a')
        f.write(url + '\n')
        f.close()
        embed = discord.Embed(description="File added to " + files[str(message.channel.id)] + " by " + str(message.author))
        await client.send_message(discord.Object(id="436544688745480203"), embed=embed)

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

    cogs = ['image', 'moderation', 'frames', 'emojibomb', 'general', 'fun', 'games', 'emojipaste']
    for cog in cogs:
        client.load_extension(cog)

    client.run(DISCORD_BOT_KEY)

if __name__ == "__main__":
    main()
