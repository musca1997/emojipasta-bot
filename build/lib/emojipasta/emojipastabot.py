"""
Generate emojipasta from text.
"""

import random
import io
import json

import emojipasta.util.emoji
import emojipasta.util.files
import emojipasta.util.text

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

client = Bot(description="Emojipasta-Bot is a dicord bot for converting text to emojipasta. \n Bot Owner: toiletplunger#8909 \n Remember to add double quotation marks when you try to &pasta long sentences. \n For example: &pasta \" this is how this bot works. \" ", command_prefix="&", pm_help = False)

class EmojipastaGenerator:

    _WORD_DELIMITER = " "
    _MAX_EMOJIS_PER_BLOCK = 2

    """Creates with default emoji mappings, loaded from a JSON file in the package.
    """
    @classmethod
    def of_default_mappings(cls):
        return EmojipastaGenerator(_get_emoji_mappings())

    """Create with custom emoji mappings.
    emoji_mappings: a dict that maps from a lowercase word to a
        list of emojis (the emojis being single-character strings).
    """
    @classmethod
    def of_custom_mappings(cls, emoji_mappings):
        return EmojipastaGenerator(emoji_mappings)

    def __init__(self, emoji_mappings):
        self._emoji_mappings = emoji_mappings

    def generate_emojipasta(self, text):
        blocks = emojipasta.util.text.split_into_blocks(text)
        new_blocks = []
        for i, block in enumerate(blocks):
            new_blocks.append(block)
            emojis = self._generate_emojis_from(block)
            if emojis:
                new_blocks.append(" " + emojis)
        return "".join(new_blocks)

    def _generate_emojis_from(self, block):
        trimmed_block = emojipasta.util.text.trim_nonalphabetical_characters(block)
        matching_emojis = self._get_matching_emojis(trimmed_block)
        emojis = []
        if matching_emojis:
            num_emojis = random.randint(0, self._MAX_EMOJIS_PER_BLOCK)
            for _ in range(num_emojis):
                emojis.append(random.choice(matching_emojis))
        return "".join(emojis)

    def _get_matching_emojis(self, trimmed_block):
        key = self._get_alphanumeric_prefix(trimmed_block.lower())
        if key in self._emoji_mappings:
            return self._emoji_mappings[self._get_alphanumeric_prefix(key)]
        return []

    def _get_alphanumeric_prefix(self, s):
        i = 0
        while i < len(s) and s[i].isalnum():
            i += 1
        return s[:i]

_EMOJI_MAPPINGS = None

def _get_emoji_mappings():
    global _EMOJI_MAPPINGS
    if _EMOJI_MAPPINGS is None:
        with io.open(emojipasta.util.files.PATH_TO_MAPPINGS_FILE, "r", encoding="utf-8") as mappings_file:
            _EMOJI_MAPPINGS = json.load(mappings_file)
    return _EMOJI_MAPPINGS

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
    	return await client.change_presence(game=discord.Game(name='DADDYS PLUNGER')) #This is buggy, let us know if it doesn't work.

    @client.command()
    async def pasta(original_words):
    	generator = EmojipastaGenerator.of_default_mappings()
    	final_emoji = generator.generate_emojipasta(original_words)

    	await client.say(final_emoji)

    @client.command()
    async def github(*args):
        await client.say("https://github.com/musca1997/emojipasta-bot")

    @client.command()
    async def orange(*args):
        await client.say("<@294963984535257089> is my best big titty goth gf <33333")

    @client.command()
    async def invite(*args):
        await client.say("https://discordapp.com/oauth2/authorize?client_id=429662497172357123&scope=bot&permissions=8")

    @client.command()
    async def stats(*args):
        await client.say(' Emojipasta-Bot \n Bot Owner: toiletplunger#8909 \n Now connected to '+str(len(client.servers))+' servers \n Connected to '+str(len(set(client.get_all_members())))+' users \n vote for me on: https://discordbots.org/bot/429662497172357123')

    @client.command()
    async def ping(*args):

    	await client.say(":ping_pong: Pong!")
    	await asyncio.sleep(1)
    	await client.say(":warning: I'M GAY")


    client.run('PUT YOUR TOKEN HERE')

if __name__ == "__main__":
    main()
