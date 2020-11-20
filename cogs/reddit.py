import discord
from discord.ext import commands
import datetime
import time
import random
import praw
reddit = praw.Reddit('ThunderousBot')
colour = 0xcdcd22
subreddit = reddit.subreddit("copypasta")

class Reddit(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def copypasta(self, ctx):
        post = subreddit.random()
        await ctx.send("**{}**".format(post.title))
        for i in range(int(len(post.selftext) / 2000) + 1):
            await ctx.send(post.selftext[(i * 2000):(i + 1) * 2000] + " ")
    
    @commands.command()
    async def redditor(self, ctx, username):
        try :
            msg = await ctx.send("Checking redditor {}...".format(username))
            user = reddit.redditor(username)
            date = time.ctime(int(user.created_utc))
            desc = "Redditor since " + str(date)

            emb = discord.Embed(title="Information for Redditor u/" + user.name, color=colour)
            emb.set_thumbnail(url=user.icon_img)
            emb.description = desc
            emb.add_field(name="Link Karma", value="{:,.0f}".format(user.link_karma), inline=True)
            emb.add_field(name="Comment Karma", value="{:,.0f}".format(user.comment_karma), inline=True)
            emb.add_field(name="Combined Karma", value="{:,.0f}".format(user.link_karma + user.comment_karma), inline=True)
            emb.timestamp = datetime.datetime.utcnow()  
            emb.set_footer(text="Bot made by Canadapost Duck#3062")
            await msg.edit(content= "", embed=emb)
        except :
            await ctx.send("There was an error in processing that redditor")

def setup(client):
    client.add_cog(Reddit(client))