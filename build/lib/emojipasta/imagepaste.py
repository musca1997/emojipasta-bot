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
import numpy as np
from random import randint
import os
os.chdir("C:\\Users\\Frankie\\Documents\\GitHub\\emojipasta-bot\\build\\lib\\emojipasta")
class Imagepaste():
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def epb(self, ctx, url: str=None):
        url = await Imagepaste.get_attachment_images(self, ctx, url)
        faces = await Imagepaste.get_face_data(self, ctx, url)

        img = Image.open(str(ctx.message.channel.id)+'.png').convert("RGBA")
        emojiface = Image.open('images/emojipasta.png').convert("RGBA")
        draw_img = img.convert("RGBA")

        for f in faces:
            w, h = f['faceRectangle']['width'], f['faceRectangle']['height']
            x, y = f['faceRectangle']['left'], f['faceRectangle']['top']

            current_emojiface = emojiface.resize((w, int(w * emojiface.size[1] / emojiface.size[0])), resample=Image.LANCZOS)
            current_emojiface = current_emojiface.rotate(f['faceAttributes']['headPose']['roll'] * -1, expand=False)

            draw_img.paste(current_emojiface, (x, y), current_emojiface)

        draw_img.save('out.png')
        await self.client.send_file(ctx.message.channel, 'out.png')

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def minion(self, ctx, url: str=None):
        url = await Imagepaste.get_attachment_images(self, ctx, url)
        faces = await Imagepaste.get_face_data(self, ctx, url)

        img = Image.open(str(ctx.message.channel.id)+'.png').convert("RGBA")
        glasses = Image.open('images/minionglasses.png').convert("RGBA")
        draw_img = img.convert("RGBA")

        for f in faces:
            w, h = f['faceRectangle']['width'], f['faceRectangle']['height']
            x, y = f['faceRectangle']['left'], f['faceRectangle']['top']

            current_emojiface = glasses.resize((w, int(w * glasses.size[1] / glasses.size[0])), resample=Image.LANCZOS)
            current_emojiface = current_emojiface.rotate(f['faceAttributes']['headPose']['roll'] * -1, expand=False)

            draw_img.paste(current_emojiface, (x, y), current_emojiface)

        draw_img.save('out.png')
        await self.client.send_file(ctx.message.channel, 'out.png')

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def lensflare(self, ctx, url: str=None):
        url = await Imagepaste.get_attachment_images(self, ctx, url)
        faces = await Imagepaste.get_face_data(self, ctx, url)

        img = Image.open(str(ctx.message.channel.id)+'.png').convert("RGBA")
        lf = Image.open('images/lensflare.png').convert("RGBA")
        draw_img = img.convert("RGBA")

        for f in faces:
            w, h = f['faceRectangle']['width'], f['faceRectangle']['height']
            left_eye = np.array([
                        [f['faceLandmarks']['eyeLeftOuter']['x'], f['faceLandmarks']['eyeLeftOuter']['y']],
                        [f['faceLandmarks']['eyeLeftBottom']['x'], f['faceLandmarks']['eyeLeftBottom']['y']],
                        [f['faceLandmarks']['eyeLeftTop']['x'], f['faceLandmarks']['eyeLeftTop']['y']],
                        [f['faceLandmarks']['eyeLeftInner']['x'], f['faceLandmarks']['eyeLeftInner']['y']]
                        ])
            right_eye = np.array([
                        [f['faceLandmarks']['eyeRightOuter']['x'], f['faceLandmarks']['eyeRightOuter']['y']],
                        [f['faceLandmarks']['eyeRightBottom']['x'], f['faceLandmarks']['eyeRightBottom']['y']],
                        [f['faceLandmarks']['eyeRightTop']['x'], f['faceLandmarks']['eyeRightTop']['y']],
                        [f['faceLandmarks']['eyeRightInner']['x'], f['faceLandmarks']['eyeRightInner']['y']]
                        ])

            left_center = left_eye.mean(axis=0).astype("int")
            right_center = right_eye.mean(axis=0).astype("int")

            current_lf = lf.resize((w, int(w * lf.size[1] / lf.size[0])), resample=Image.LANCZOS)
            current_lf = current_lf.rotate((f['faceAttributes']['headPose']['roll'] * -1) + 45, expand=True)

            w_offset, h_offset = int(current_lf.width / 2), int(current_lf.height / 2)
            draw_img.paste(current_lf, (left_center[0] - w_offset, left_center[1] - h_offset), current_lf)
            draw_img.paste(current_lf, (right_center[0] - w_offset, right_center[1] - h_offset), current_lf)

        draw_img.save('out.png')
        await self.client.send_file(ctx.message.channel, 'out.png')

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def hearteyes(self, ctx, url: str=None):
        url = await Imagepaste.get_attachment_images(self, ctx, url)
        faces = await Imagepaste.get_face_data(self, ctx, url)

        img = Image.open(str(ctx.message.channel.id)+'.png').convert("RGBA")
        lf = Image.open('images/heart.png').convert("RGBA")
        draw_img = img.convert("RGBA")

        for f in faces:
            w, h = f['faceRectangle']['width'], f['faceRectangle']['height']
            left_eye = np.array([
                        [f['faceLandmarks']['eyeLeftOuter']['x'], f['faceLandmarks']['eyeLeftOuter']['y']],
                        [f['faceLandmarks']['eyeLeftBottom']['x'], f['faceLandmarks']['eyeLeftBottom']['y']],
                        [f['faceLandmarks']['eyeLeftTop']['x'], f['faceLandmarks']['eyeLeftTop']['y']],
                        [f['faceLandmarks']['eyeLeftInner']['x'], f['faceLandmarks']['eyeLeftInner']['y']]
                        ])
            right_eye = np.array([
                        [f['faceLandmarks']['eyeRightOuter']['x'], f['faceLandmarks']['eyeRightOuter']['y']],
                        [f['faceLandmarks']['eyeRightBottom']['x'], f['faceLandmarks']['eyeRightBottom']['y']],
                        [f['faceLandmarks']['eyeRightTop']['x'], f['faceLandmarks']['eyeRightTop']['y']],
                        [f['faceLandmarks']['eyeRightInner']['x'], f['faceLandmarks']['eyeRightInner']['y']]
                        ])

            left_center = left_eye.mean(axis=0).astype("int")
            right_center = right_eye.mean(axis=0).astype("int")
            current_lf = lf.resize((int(w * .45), int(int(w * .45) * lf.size[1] / lf.size[0])), resample=Image.LANCZOS)

            w_offset, h_offset = int(current_lf.width / 2), int(current_lf.height / 2)
            leftheart = current_lf.rotate((f['faceAttributes']['headPose']['roll'] * -1) + 20, expand=False)
            rightheart = current_lf.rotate((f['faceAttributes']['headPose']['roll'] * -1) - 20, expand=False)

            draw_img.paste(leftheart, (left_center[0] - w_offset, left_center[1] - h_offset), leftheart)
            draw_img.paste(rightheart, (right_center[0] - w_offset, right_center[1] - h_offset), rightheart)

        draw_img.save('out.png')
        await self.client.send_file(ctx.message.channel, 'out.png')

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def mlp(self, ctx, url: str=None):
        url = await Imagepaste.get_attachment_images(self, ctx, url)
        faces = await Imagepaste.get_face_data(self, ctx, url)

        img = Image.open(str(ctx.message.channel.id)+'.png').convert("RGBA")
        draw_img = img.convert("RGBA")

        for f in faces:
            r = randint(0,5)
            eyes = Image.open('images/mlp'+str(r)+'.png').convert("RGBA")

            w, h = f['faceRectangle']['width'], f['faceRectangle']['height']
            x, y = f['faceRectangle']['left'], f['faceRectangle']['top']

            current_emojiface = eyes.resize((w, int(w * eyes.size[1] / eyes.size[0])), resample=Image.LANCZOS)
            current_emojiface = current_emojiface.rotate(f['faceAttributes']['headPose']['roll'] * -1, expand=False)

            draw_img.paste(current_emojiface, (x, y), current_emojiface)

        draw_img.save('out.png')
        await self.client.send_file(ctx.message.channel, 'out.png')

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def thuglife(self, ctx, url: str=None):
        url = await Imagepaste.get_attachment_images(self, ctx, url)
        faces = await Imagepaste.get_face_data(self, ctx, url)

        img = Image.open(str(ctx.message.channel.id)+'.png').convert("RGBA")
        glasses = Image.open('images/dealwithit.png').convert("RGBA")
        joint = Image.open('images/joint.png').convert("RGBA")
        draw_img = img.convert("RGBA")

        for f in faces:
            w, h = f['faceRectangle']['width'], f['faceRectangle']['height']
            nose = np.array([
                        [f['faceLandmarks']['noseRootLeft']['x'], f['faceLandmarks']['noseRootLeft']['y']],
                        [f['faceLandmarks']['noseRootRight']['x'], f['faceLandmarks']['noseRootRight']['y']]
                        ])

            nose_center = nose.mean(axis=0).astype("int")
            center_lip_y = abs((int(f['faceLandmarks']['upperLipTop']['y']) - int(f['faceLandmarks']['underLipBottom']['y'])) / 2)
            final_y = int(f['faceLandmarks']['upperLipTop']['y'] + center_lip_y)
            w2 = int(abs(f['faceLandmarks']['mouthLeft']['x'] - f['faceLandmarks']['mouthRight']['x']))
            final_x = int((w2 / 2) + f['faceLandmarks']['mouthLeft']['x'])

            current_glasses = glasses.resize((w, int(w * glasses.size[1] / glasses.size[0])), resample=Image.LANCZOS)
            current_glasses = current_glasses.rotate(f['faceAttributes']['headPose']['roll'] * -1, expand=True)
            offset_x, offset_y = int(current_glasses.width / 2), int(current_glasses.height / 2)

            new_joint = joint.resize((int(w2 * .75), int((w2 * .75) * joint.size[1] / joint.size[0])), resample=Image.LANCZOS)
            new_joint = new_joint.rotate(f['faceAttributes']['headPose']['roll'] * -1, expand=False)

            draw_img.paste(current_glasses, (nose_center[0] - offset_x, nose_center[1] - offset_y), current_glasses)
            draw_img.paste(new_joint, (final_x, final_y), new_joint)

        draw_img.save('out.png')
        await self.client.send_file(ctx.message.channel, 'out.png')

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def mood(self, ctx, url: str=None):
        url = await Imagepaste.get_attachment_images(self, ctx, url)
        faces = await Imagepaste.get_face_data(self, ctx, url)

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

    async def get_face_data(self, ctx, url):
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
        return faces

def setup(client):
    client.add_cog(Imagepaste(client))
