import discord
from discord.ext import commands
from random import randint
from discord.ext.commands.cooldowns import BucketType
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import urllib.request
import os

class Frames():
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="zucc1 zucc2 zucc3")
    async def zucc(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def zucc1(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def zucc2(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def zucc3(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def ifunny(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def funwaa(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="idub1 idub2 idub3 idub4 idub5 idub6")
    async def idub(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def idub1(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def idub2(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def idub3(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def idub4(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def idub5(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def idub6(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def shutterstock(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def commie(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def gay(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def kek(self):
        pass

    async def on_command(self, command, ctx):
        if command.description:
            split = command.description.split()
            rand = randint(0, len(split) - 1)
            command = str(split[rand])

        command = str(command)
        frame = "frames/"+command+".png"
        picture = str(ctx.message.channel.id)+'.png'
        await Frames.filtered_image(self, ctx, picture, frame)
        await self.client.send_file(ctx.message.channel, picture)

    async def filtered_image(self, ctx, pic_name, chosen_filter):
        await Frames.get_attachment_images(self, ctx)
        background = Image.open(pic_name)
        w, h = background.size
        foreground = Image.open(chosen_filter)
        foreground = foreground.resize((w,h), Image.ANTIALIAS)
        background.paste(foreground, (0, 0), foreground)
        background.save(pic_name)

    async def get_attachment_images(self, ctx):
        last_attachment = None
        async for m in self.client.logs_from(ctx.message.channel, before=ctx.message, limit=20):
            if m.attachments:
                last_attachment = m.attachments[0]['url']
                break
        pic_name = str(ctx.message.channel.id)+'.png'
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        f = urllib.request.Request(url=last_attachment,headers=headers)
        f = urllib.request.urlopen(f)
        with open(pic_name, "wb") as c:
            c.write(f.read())

def setup(client):
    client.add_cog(Frames(client))
