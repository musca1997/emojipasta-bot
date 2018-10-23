import discord
from discord.ext import commands
from random import randint
from discord.ext.commands.cooldowns import BucketType
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import urllib.request
from util.functions import Functions

class Frames():
    def __init__(self, client):
        self.client = client

#meme frames
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame zucc1 zucc2 zucc3 zucc4")
    async def zucc(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def zucc1(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def zucc2(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def zucc3(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def zucc4(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def ifunny(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def funwaa(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def ss(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame idub1 idub2 idub3 idub4 idub5 idub6")
    async def idub(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub1(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub2(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub3(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub4(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub5(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def idub6(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame swear1 swear2")
    async def swear(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def swear1(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def swear2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def shutterstock(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def commie(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def gay(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def kek(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def preg(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def trigger(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cat(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def kim(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def sonic(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def tp(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def gag(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def knuckle(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def liberal(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def pickle(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def sb(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def nut(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def altright(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def buzzfeed(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def die(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cry(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def dick(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def unlock(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def hillary(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def shrek(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def mark(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def memri(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def wish(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def porn(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def sam(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def wasted(self):
        pass

#music frames

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame coil1 coil2")
    async def coil(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def coil1(self):
        pass
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def coil2(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def dg(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def viper(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def lrd(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def nmh(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def television(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def blond(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def ac(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def vu(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def lilpeep(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def lilpump(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def madvillainy(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def beatles(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def bjork(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def can(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def qotsa(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def swans(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def sy(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def damn(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def rh(self):
        pass

#film frames
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def cowboy(self):
        pass

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(description="frame")
    async def lynch(self):
        pass
#func thinggy
    async def on_command(self, command, ctx):
        if not command.description:
            return
        split = command.description.split()
        if len(split) > 1:
            rand = randint(0, len(split) - 1)
            command = str(split[rand])
        await self.client.say("**processing...**")
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
                if len(m.attachments) > 0 and 'url' in m.attachments[0]:
                    last_attachment = m.attachments[0]['url']
                    if not Functions.is_image(last_attachment):
                        continue
                    else:
                        break
                else:
                    continue
            elif m.embeds:
                if len(m.embeds) > 0 and 'url' in m.embeds[0]:
                    last_attachment = m.embeds[0]['url']
                    if not Functions.is_image(last_attachment):
                        continue
                    else:
                        break
                else:
                    continue
        pic_name = str(ctx.message.channel.id)+'.png'
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        f = urllib.request.Request(url=last_attachment,headers=headers)
        f = urllib.request.urlopen(f)
        with open(pic_name, "wb") as c:
            c.write(f.read())

def setup(client):
    client.add_cog(Frames(client))
