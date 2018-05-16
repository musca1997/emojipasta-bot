import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
from random import randint
import urllib.request

class Bot_Image_Filter():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def blur(self, ctx, url: str=None):
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.get_attachment_images(self, ctx, url)
        original = Image.open(pic_name)
        blurred = original.filter(ImageFilter.BLUR)
        blurred.save(pic_name)
        await self.client.send_file(ctx.message.channel, pic_name)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def glitch(self, ctx, url: str=None):
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.get_attachment_images(self, ctx, url)
        img = Image.open(pic_name)
        img = img.convert('RGB')
        w, h = img.width, img.height
        img = img.resize((int(w ** .75), int(h ** .75)), resample=Image.LANCZOS)
        img = img.resize((int(w ** .88), int(h ** .88)), resample=Image.BILINEAR)
        img = img.resize((int(w ** .9), int(h ** .9)), resample=Image.BICUBIC)
        img = img.resize((w, h), resample=Image.BICUBIC)
        img = ImageOps.posterize(img, 4)
        r = img.split()[0]
        r = ImageEnhance.Contrast(r).enhance(10.0)
        r = ImageEnhance.Brightness(r).enhance(1.5)
        img = ImageEnhance.Sharpness(img).enhance(100.0)
        img.save(pic_name)
        await self.client.send_file(ctx.message.channel, pic_name)

    async def get_attachment_images(self, ctx, url):
        last_attachment = None
        if url is None:
            async for m in self.client.logs_from(ctx.message.channel, before=ctx.message, limit=20):
                if m.attachments:
                    last_attachment = m.attachments[0]['url']
                    break
                elif m.embeds:
                    last_attachment = m.embeds[0]['url']
                    break
        else:
            last_attachment = url
        pic_name = str(ctx.message.channel.id)+'.png'
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        f = urllib.request.Request(url=last_attachment,headers=headers)
        f = urllib.request.urlopen(f)
        with open(pic_name, "wb") as c:
            c.write(f.read())

def setup(client):
    client.add_cog(Bot_Image_Filter(client))
