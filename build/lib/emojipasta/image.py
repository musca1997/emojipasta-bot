import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
from random import randint
import urllib.request

class Bot_Image_Filter():
    def __init__(self, client):
        self.client = client

    async def log(self, command, server, time):
        embed = discord.Embed(description="used the " + command + " command.", timestamp=time)
        embed.set_author(name=server)
        await self.client.send_message(discord.Object(id="436544688745480203"), embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def blur(self, ctx, *args):
        await self.client.say("**Processing Image...(Note: In order to prevent spam, you can only use filter funcs once every 15s.)**")
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.get_attachment_images(self, ctx)
        original = Image.open(pic_name)
        blurred = original.filter(ImageFilter.BLUR)
        blurred.save(pic_name)
        await self.client.send_file(ctx.message.channel, pic_name)
        await Bot_Image_Filter.log(self, "blur", ctx.message.server, ctx.message.timestamp)

    @commands.command(pass_context=True)
    async def ifunny(self, ctx, *args):
        await self.client.say("**Processing Image...(Note: In order to prevent spam, you can only use filter funcs once every 15s.)**")
        chosen_filter = 'filters/ifunny.png'
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.filtered_image(self, ctx, pic_name, chosen_filter)
        await self.client.send_file(ctx.message.channel, pic_name)
        await Bot_Image_Filter.log(self, "ifunny", ctx.message.server, ctx.message.timestamp)

    @commands.command(pass_context=True)
    async def gay(self, ctx, *args):
        await self.client.say("**Processing Image...(Note: In order to prevent spam, you can only use filter funcs once every 15s.)**")
        chosen_filter = 'filters/gay.png'
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.filtered_image(self, ctx, pic_name, chosen_filter)
        await self.client.send_file(ctx.message.channel, pic_name)
        await Bot_Image_Filter.log(self, "gay", ctx.message.server, ctx.message.timestamp)

    @commands.command(pass_context=True)
    async def ss(self, ctx, *args):
        await self.client.say("**Processing Image...(Note: In order to prevent spam, you can only use filter funcs once every 15s.)**")
        chosen_filter = 'filters/shutterstock.png'
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.filtered_image(self, ctx, pic_name, chosen_filter)
        await self.client.send_file(ctx.message.channel, pic_name)
        await Bot_Image_Filter.log(self, "ss", ctx.message.server, ctx.message.timestamp)

    @commands.command(pass_context=True)
    async def funwaa(self, ctx, *args):
        await self.client.say("**Processing Image...(Note: In order to prevent spam, you can only use filter funcs once every 15s.)**")
        chosen_filter = 'filters/funwaa.png'
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.filtered_image(self, ctx, pic_name, chosen_filter)
        await self.client.send_file(ctx.message.channel, pic_name)
        await Bot_Image_Filter.log(self, "funwaa", ctx.message.server, ctx.message.timestamp)

    @commands.command(pass_context=True)
    async def commie(self, ctx, *args):
        await self.client.say("**Processing Image...(Note: In order to prevent spam, you can only use filter funcs once every 15s.)**")
        chosen_filter = 'filters/commie.png'
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.filtered_image(self, ctx, pic_name, chosen_filter)
        await self.client.send_file(ctx.message.channel, pic_name)
        await Bot_Image_Filter.log(self, "commie", ctx.message.server, ctx.message.timestamp)

    @commands.command(pass_context=True)
    async def kek(self, ctx, *args):
        await self.client.say("**Processing Image...(Note: In order to prevent spam, you can only use filter funcs once every 15s.)**")
        chosen_filter = 'filters/kek.png'
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.filtered_image(self, ctx, pic_name, chosen_filter)
        await self.client.send_file(ctx.message.channel, pic_name)
        await Bot_Image_Filter.log(self, "kek", ctx.message.server, ctx.message.timestamp)

    @commands.command(pass_context=True)
    async def zucc(self, ctx, *args):
        await self.client.say("**Processing Image...(Note: In order to prevent spam, you can only use filter funcs once every 15s.)**")
        zucc_list = ['filters/zucc1.png', 'filters/zucc2.png', 'filters/zucc3.png']
        num = randint(0, len(zucc_list)-1)
        chosen_filter = zucc_list[num]
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.filtered_image(self, ctx, pic_name, chosen_filter)
        await self.client.send_file(ctx.message.channel, pic_name)
        await Bot_Image_Filter.log(self, "zucc", ctx.message.server, ctx.message.timestamp)

    @commands.command(pass_context=True)
    async def glitch(self, ctx, *args):
        await self.client.say("**Processing Image...(Note: In order to prevent spam, you can only use filter funcs once every 15s.)**")
        pic_name = str(ctx.message.channel.id)+'.png'
        await Bot_Image_Filter.get_attachment_images(self, ctx)
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
        await Bot_Image_Filter.log(self, "glitch", ctx.message.server, ctx.message.timestamp)


    async def filtered_image(self, ctx, pic_name, chosen_filter):
        await Bot_Image_Filter.get_attachment_images(self, ctx)
        background = Image.open(pic_name)
        w, h = background.size
        foreground = Image.open(chosen_filter)
        foreground = foreground.resize((w,h), Image.ANTIALIAS)
        background.paste(foreground, (0, 0), foreground)
        background.save(pic_name)


    async def get_attachment_images(self, ctx):
        last_attachment = None
        img_urls = []
        async for m in self.client.logs_from(ctx.message.channel, before=ctx.message, limit=20):
            if m.attachments:
                last_attachment = m.attachments[0]['url']
                img_urls.append(last_attachment)
        num = len(img_urls)-1
        last_url = img_urls[0]
        pic_name = str(ctx.message.channel.id)+'.png'
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        f = urllib.request.Request(url=last_url,headers=headers)
        f = urllib.request.urlopen(f)
        with open(pic_name, "wb") as c:
            c.write(f.read())

def setup(client):
    client.add_cog(Bot_Image_Filter(client))
