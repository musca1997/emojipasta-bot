from util.keys import AZURE_API_KEY
import asyncio, aiohttp, discord
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
import json
import urllib.request
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from util.functions import Functions

class Emojipaste():
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def epb(self, ctx, url: str=None):
        url = await Emojipaste.get_attachment_images(self, ctx, url)
        headers = {"Content-Type":"application/json", "Ocp-Apim-Subscription-Key": AZURE_API_KEY}
        data = {"url": url}
        faces = {}
        async with aiohttp.ClientSession() as session:
            async with session.post('https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=false&returnFaceLandmarks=true&returnFaceAttributes=headPose', headers=headers, data=json.dumps(data)) as r:
                faces = await r.json()

        if len(faces) == 0:
            await self.client.say(":no_entry_sign: Unable to detect a face.")
            return
        if "error" in faces:
            await self.client.say(":warning: API error returned. Try again later.")
            return

        img = Image.open(str(ctx.message.channel.id)+'.png').convert("RGBA")
        emojiface = Image.open('images/emojipasta.png').convert("RGBA")

        draw_img = img.convert("RGBA")
        for f in faces:
            w, h = f['faceRectangle']['width'], f['faceRectangle']['height']
            x, y = f['faceRectangle']['left'], f['faceRectangle']['top']
            current_emojiface = emojiface.resize((w + int(w * .2), int((w + int(w * .2)) * emojiface.size[1] / emojiface.size[0])), resample=Image.LANCZOS)
            current_emojiface = current_emojiface.rotate(f['faceAttributes']['headPose']['roll'] * -1, expand=False)
            draw_img.paste(current_emojiface, (x, y), current_emojiface)

        draw_img.save('out.png')
        await self.client.send_file(ctx.message.channel, 'out.png')


    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def mood(self, ctx, url: str=None):
        url = await Emojipaste.get_attachment_images(self, ctx, url)
        headers = {"Content-Type":"application/json", "Ocp-Apim-Subscription-Key": AZURE_API_KEY}
        data = {"url": url}
        faces = {}
        async with aiohttp.ClientSession() as session:
            async with session.post('https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=false&returnFaceLandmarks=true&returnFaceAttributes=headPose,emotion,glasses', headers=headers, data=json.dumps(data)) as r:
                faces = await r.json()

        if len(faces) == 0:
            await self.client.say(":no_entry_sign: Unable to detect a face.")
            return
        if "error" in faces:
            await self.client.say(":warning: API error returned. Try again later.")
            return

        img = Image.open(str(ctx.message.channel.id)+'.png').convert("RGBA")
        draw_img = img.convert("RGBA")

        for f in faces:
            d = {}
            for emotion, value in f['faceAttributes']['emotion'].items():
                d[emotion] = value

            emotion = ""
            if f['faceAttributes']['glasses'] == "Sunglasses":
                emotion = "sunglasses"
            else:
                v = list(d.values())
                k = list(d.keys())
                emotion = k[v.index(max(v))]

            emojiface = Image.open('images/'+emotion+'.png').convert("RGBA")
            w, h = f['faceRectangle']['width'], f['faceRectangle']['height']
            x, y = f['faceRectangle']['left'], f['faceRectangle']['top']
            current_emojiface = emojiface.resize((w, int(w * emojiface.size[1] / emojiface.size[0])), resample=Image.LANCZOS)
            current_emojiface = current_emojiface.rotate(f['faceAttributes']['headPose']['roll'] * -1, expand=False)
            draw_img.paste(current_emojiface, (x, y), current_emojiface)

        draw_img.save('out.png')
        await self.client.send_file(ctx.message.channel, 'out.png')

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
        return last_attachment

def setup(client):
    client.add_cog(Emojipaste(client))
