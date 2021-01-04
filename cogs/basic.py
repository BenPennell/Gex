import discord
from discord.ext import commands
import random

endings = ("or", "er", "ur", "ire")
emotes = (":zany_face:", ":rofl:", ":smirk:", ":sunglasses:")
jokes = True
inFile = open("GexVoiceLines.txt")
gexLines = inFile.readlines()

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    # sets the status of the bot
    async def on_ready(self):
        activity = discord.Game(name="Gex: Enter the Gecko", type=3)
        await self.client.change_presence(status=discord.Status.online, activity=activity)
        print('GexBot is up and running')
    
    @commands.Cog.listener()
    # listens for words with specific endings to make a joke
    async def on_message(self, message):
        if jokes == True:
            if message.author != self.client.user:
                if random.random() < 0.25: # make jokes only have a 25% chance of happening
                    # I BARELY EVEN KNEW HER HAHAHAHAHAHA
                    content = message.content.lower()
                    words = content.split()
                    for word in words:
                        # ends with an ending, has len 5 or more
                        if word.endswith(endings) and len(word) >= 5:
                            # HAHAHAHAHAHAHAHAHAHAH (laugh)
                            await message.channel.send("{}? I barely even knew her! {}".format(word, random.choice(emotes)))
                            break

    
    @commands.command(brief="DUCC ONLY. Toggles on/off jokes")
    # turns the jokes on/off
    async def toggleJokes(self, ctx):
        if ctx.author.id == 287060396953698305:
            global jokes
            jokes = not jokes
            await ctx.send("jokes enabled: {}".format(jokes))
        else:
            await ctx.send("You do not have permission to do that. Jokes enabled: {}".format(jokes))
    
    @commands.command(brief="Get a random gex voiceline")
    # gets a random line from the gexVoiceLines file
    async def gex(self, ctx):
        await ctx.send(random.choice(gexLines))
    
    @commands.command(brief="Use >rand [number] to get a random number 1-[number]")
    # generates a random number from 1 - input
    async def rand(self, ctx):
        content = (ctx.message.content[6:]).strip()
        if content.isnumeric():
            await ctx.send(":thinking: alright here's a number between 1 and {}: **{}**".format(int(content), random.randint(1, int(content))))
        else:
            await ctx.send("Try >rand [number] for a specific interval. Here's a random number though: {}".format(random.random()))

def setup(client):
    client.add_cog(Basic(client))