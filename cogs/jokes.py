import discord
from discord.ext import commands
import random

endings = ("or", "er", "ur", "ire")
emotes = (":zany_face:", ":rofl:", ":smirk:", ":sunglasses:")

class Jokes(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.client.user:
            # I BARELY EVEN KNEW HER HAHAHAHAHAHA
            content = message.content.lower()
            words = content.split()
            for word in words:
                # ends with an ending, has len 5 or more and only 25% chance
                if word.endswith(endings) and len(word) >= 5 and random.random() < 0.25:
                    # HAHAHAHAHAHAHAHAHAHAH (laugh)
                    await message.channel.send("{}? I barely even knew her! {}".format(word, random.choice(emotes)))
                    break

def setup(client):
    client.add_cog(Jokes(client))