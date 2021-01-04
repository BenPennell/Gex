import discord
from discord.ext import commands
import datetime
import time
import random
import praw
reddit = praw.Reddit('')
colour = 0xcdcd22
copypasta = reddit.subreddit("copypasta")
dankmemes = reddit.subreddit("dankmemes")
memesubs = [reddit.subreddit("dankmemes"), reddit.subreddit("dogelore")]
class Reddit(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(brief="Get a random copypasta")
    async def copypasta(self, ctx):
        post = copypasta.random()
        await ctx.send("**{}**".format(post.title))
        for i in range(int(len(post.selftext) / 2000) + 1):
            await ctx.send(post.selftext[(i * 2000):(i + 1) * 2000] + " ")
    
    @commands.command(brief="get a random meme from reddit")
    async def meme(self, ctx):
        sub = random.choice(memesubs)
        print(sub.display_name)
        post = sub.random()
        print(post)
        emb = discord.Embed(title = "Post on r/{} by u/{}".format(sub.display_name, post.author.name), color=colour)
        emb.description = title="[{}](https://www.reddit.com{})".format(post.title, post.permalink)
        emb.set_image(url=post.url)
        emb.add_field(name="This post was made on {}".format(datetime.datetime.fromtimestamp(post.created_utc)), value="And has {} upvotes".format(post.score))
        emb.timestamp = datetime.datetime.utcnow()  
        emb.set_footer(text="Bot made by Canadapost Duck#3062")
        await ctx.send(embed=emb)

    @commands.command(brief="Use >redditor [username] to get info about a redditor")
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