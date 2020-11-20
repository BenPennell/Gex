import discord
from discord.ext import commands
import random

emotes = (":zany_face:", ":rofl:", ":smirk:", ":sunglasses:")
inFile = open("GexVoiceLines.txt")
gexLines = inFile.readlines()

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name="In a pond", type=3)
        await self.client.change_presence(status=discord.Status.online, activity=activity)
        print('DuccBot is up and running')
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong {}".format(random.choice(emotes)))
    
    @commands.command()
    async def gex(self, ctx):
        await ctx.send(random.choice(gexLines))

def setup(client):
    client.add_cog(Basic(client))