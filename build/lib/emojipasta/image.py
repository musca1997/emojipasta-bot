import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
from random import randint
import urllib.request
from util.functions import Functions
import math

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
    async def df(self, ctx, url: str=None):
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.get_attachment_images(self, ctx, url)
        original = Image.open(pic_name)
        df = original.filter(ImageFilter.EDGE_ENHANCE)
        df = df.filter(ImageFilter.SHARPEN)
        df = df.filter(ImageFilter.EDGE_ENHANCE_MORE)
        df = df.filter(ImageFilter.SMOOTH)


        deep = ImageEnhance.Contrast(df)
        df = deep.enhance(15)

        df.save(pic_name)
        await self.client.send_file(ctx.message.channel, pic_name)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def shrink(self, ctx, per: str=None, url: str=None):
        if not (per is None and url is None):
            try:
                per = int(per)
                if per == 100:
                    await self.client.say(":no_entry_sign: You're trying to shrink an image to 100% of it's size. Percentage defaulted to 5%")
                    per = 5
                if per > 100:
                    await self.client.say(":no_entry_sign: This is the *shrink* command. Percentage defaulted to 5%")
                    per = 5
            except:
                url = per
                per = 5
        else:
            per = 5
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.get_attachment_images(self, ctx, url)
        img = Image.open(pic_name).convert("RGBA")
        w, h = img.width, img.height
        img = img.resize((int(w * (per * .01)), int(h * (per * .01))), resample=Image.LANCZOS)
        img.save(pic_name)
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

    @commands.command(pass_context=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def edges(self, ctx, url: str=None):
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.get_attachment_images(self, ctx, url)
        img = Image.open(pic_name).convert("RGBA")
        width, height = img.width, img.height
        newimg = Image.new("RGB", (width, height), "white")
        for x in range(1, width-1):
            for y in range(1, height-1): 1)
                Gx = 0
                Gy = 0
                p = img.getpixel((x-1, y-1))
                r = p[0]
                g = p[1]
                b = p[2]
                intensity = r + g + b
                Gx += -intensity
                Gy += -intensity
                p = img.getpixel((x-1, y))
                r = p[0]
                g = p[1]
                b = p[2]
                Gx += -2 * (r + g + b)
                p = img.getpixel((x-1, y+1))
                r = p[0]
                g = p[1]
                b = p[2]
                Gx += -(r + g + b)
                Gy += (r + g + b)
                p = img.getpixel((x, y-1))
                r = p[0]
                g = p[1]
                b = p[2]
                Gy += -2 * (r + g + b)
                p = img.getpixel((x, y+1))
                r = p[0]
                g = p[1]
                b = p[2]
                Gy += 2 * (r + g + b)
                p = img.getpixel((x+1, y-1))
                r = p[0]
                g = p[1]
                b = p[2]
                Gx += (r + g + b)
                Gy += -(r + g + b)
                p = img.getpixel((x+1, y))
                r = p[0]
                g = p[1]
                b = p[2]
                Gx += 2 * (r + g + b)
                p = img.getpixel((x+1, y+1))
                r = p[0]
                g = p[1]
                b = p[2]
                Gx += (r + g + b)
                Gy += (r + g + b)
                length = math.sqrt((Gx * Gx) + (Gy * Gy))
                length = length / 4328 * 255
                length = int(length)
                newimg.putpixel((x,y),(length,length,length))
        newimg.save(pic_name)
        await self.client.send_file(ctx.message.channel, pic_name)

    async def get_attachment_images(self, ctx, url):
        last_attachment = url
        if url:
            if Functions.is_image(url) is False:
                url = None
        if url is None:
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
    client.add_cog(Bot_Image_Filter(client))
