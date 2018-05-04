import discord
from discord.ext import commands

class Help():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def help(self, ctx, message: str=None):
        embed = discord.Embed(title="Kermit Klan House", colour=discord.Colour(0xa4302c), url="https://discord.gg/JHNRwr6", description="Emojipasta-Bot is a bot mainly for converting text to emojipasta.")
        embed.colour = 0xfce74a
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/419521490220744705/429667256717279262/f42b7e7.png")
        embed.set_author(name="Emojipasta-Bot Info", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/attachments/419521490220744705/429667256717279262/f42b7e7.png")
        embed.set_footer(text="Powered by Kermit Klan House", icon_url="https://cdn.discordapp.com/attachments/419521490220744705/429667256717279262/f42b7e7.png")

        descriptions = {
            "pasta": "pasta <message>\nConverts your text into delicious emojipasta",
            "clap": "clap <message>\nAdds various clap emojis inbetween words",
            "yn": "yn <question>\nGenerates a random yes or no response",
            "rn": "rn <lower bound> <upper bound>\nGenerates a random number between the supplied interval. If no interval is given, it will default to 1-100.",
            "b": "b <message>\nAny letter 'b' within the message will be replaced with 🅱️. This command is not case-sensitive.",
            "owo": "owo <message>\nCweate wovable text with this command. Replaces any 'r' or 'l' in your message with 'w'",
            "qr": "qr <text>\nGenerates a QR code with the given text string.",
            "penislength": "penislength <@user>\nFind out the penis length of the specified user. Omit the tag to find out your own penis length.",
            "mock": "mock <message>\nMock someone you can't stand. MoCk SoMeOnE yOu CaN't StAnD.",
            "userinfo": "userinfo <@user>\nDisplays information about a tagged user. Omit the tag to find out information about yourself.",
            "serverinfo": "serverinfo\nDisplays information about the server the command was invoked on.",
            "jerkit": "jerkit\nRelease some stress by jerkin' it.\n**Cooldown:** 5 minutes.",
            "walk": "walk <@user>\nTake the tagged user for a walk. Omit the tag to prompt the channel if anyone would like to go for a walk.",
            "dab": "dab <@user>\nTake a moment to dab on the tagged user. Omit the tag to dab the entire channel the command was invoked in.",
            "spin": "spin <@user>\nBust out your fidget spinner and spin on the tagged user. Omit the tag to spin on the entire channel the command was invoked in.",
            "brawl": "brawl <@user1> <@user2> (optional) <@user3> <@user4> <@user5>\nDuke it out and start a brawl with up to 5 tagged members. Minimum of two users required.",
            "ban": "ban <@user>\nBans the specified user from the server. Reserved for roles with the necessary permissions.",
            "kick": "kick <@user>\nKicks the specified user from the server. Reserved for roles with the necessary permissions.",
            "nick": "nick <@user> <nickname>\nChanges the nickname of the tagged user to a nickname of your choosing.",
            "flip": "flip <message>\nTakes your message and flips it upside down.",
            "ud": "ud <search term>\nSearch Urban Dictionary for the specified term.",
            "d": "d\nSings one of the most famous lyrics of all time.\n**Cooldown:** 1 minute.",
            "uw": "uw\nSelects a random useless website and displays it to the channel.",
            "bw": "bw\nYa'll ever want to flex on Chinese users? Displays a website that is banned in China.",
            "ping": "ping\nUsed as a test command to make sure the bot is working."
        }
        if message:
            commandembed = discord.Embed(title="&" + message, description="**Syntax:** &" + descriptions[message])
            commandembed.colour = 0xfce74a
            commandembed.set_author(name="Emojipasta-Bot Info", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/attachments/419521490220744705/429667256717279262/f42b7e7.png")
            await self.client.say(embed=commandembed)
            return

        fields = [
            ["pasta", "Convert text to emojipasta"],
            ["clap", "Add clap emojis between words"],
            ["yn", "Make a yes or no decision"],
            ["rn", "Generates a random number"],
            ["b", "Replace any letter 'b' with 🅱️"],
            ["owo", "You wiww weawwy wove this one"],
            ["qr", "Generate a QR code"],
            ["penislength", "Measure penislength"],
            ["mock", "Use &mock with text to gEt cOoL tExT."],
            ["userinfo", "Use &userinfo or &serverinfo to get the information."],
            ["jerkit", "Use &jerkit to jerk off when you can't jerk off."],
            ["walk/&dab/&spin/&brawl", "Use one of these commands with @someone to interact with them!"],
            ["ban/&kick/&nick", "Only higher roles of the server can use these functions."],
            ["flip", "uʍop ǝpᴉsdn ʇxǝʇ ɹnoʎ dᴉlɟ"],
            ["ud", "Use &ud <term> to search Urban Dictionary!"],
            ["d", "DES PA CI TO. Can only be used once every min."],
            ["uw/&bw/&d", "Useless commands but why not try?"],
            ["ping", "Nothing special. Just to test if bot is working."],
        ]

        embed.add_field(name="Use &help <command> to find out more information about a specific command.\nUse &feedback <message> to report any bugs or to make a suggestion.", value="Enjoy!")
        for command, description in fields:
        	embed.add_field(name="**&" + command + "**", value=description, inline=False)

        embed.add_field(name="💬", value=str(len(self.client.servers))+ ' **servers**', inline=True)
        embed.add_field(name="🏠", value=str(len(set(self.client.get_all_members())))+ ' **users**', inline=True)
        embed.add_field(name="👁", value="[support](https://discord.gg/JHNRwr6)", inline=True)
        embed.add_field(name="💦", value="[github](https://github.com/musca1997/emojipasta-bot)", inline=True)
        embed.add_field(name="💯", value="[vote](https://discordbots.org/bot/429662497172357123)", inline=True)
        embed.add_field(name="😎", value="[invite](https://discordapp.com/oauth2/authorize?client_id=429662497172357123&scope=bot&permissions=8)", inline=True)

        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(Help(client))
