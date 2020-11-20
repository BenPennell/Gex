'''
this is UNUSED
TESTING CODE
kept it for nostalgia :)
import discord
import datetime
import time
import random
import praw
reddit = praw.Reddit('ThunderousBot')
client = discord.Client()
colour = 0xcdcd22
subreddit = reddit.subreddit("copypasta")

endings = ("or", "er", "ur", "ire")
emotes = (":zany_face:", ":rofl:", ":smirk:", ":sunglasses:")

# log in
@client.event
async def on_ready():
    activity = discord.Game(name="In a pond", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('{0.user} is up and running'.format(client))

# for each message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content.lower()

    if content.startswith(">"):
        content = content[1:]
    #-----------------------------------------------------------------------Test
    if content == "ping":
        await message.channel.send("Pong {}".format(random.choice(emotes)))

    elif content == "copypasta":
        post = subreddit.random()
        await message.channel.send("**{}**".format(post.title))
        for i in range(int(len(post.selftext) / 2000) + 1):
            await message.channel.send(post.selftext[(i * 2000):(i + 1) * 2000] + " ")
    #-----------------------------------------------------------------------Karma Breakdown
    elif content.startswith("redditor ") :
        content = content[9:]
    
        try :
            user = reddit.redditor(content)
            date = time.ctime(int(user.created_utc))
            desc = "Redditor since " + str(date)

            emb = discord.Embed(title="Information for Redditor u/" + user.name, color=colour)
            emb.set_thumbnail(url=user.icon_img)
            emb.description = desc
            emb.add_field(name="Link Karma", value="{:,.0f}".format(user.link_karma), inline=True)
            emb.add_field(name="Comment Karma", value="{:,.0f}".format(user.comment_karma), inline=True)
            emb.add_field(name="Combined Karma", value="{:,.0f}".format(user.link_karma + user.comment_karma), inline=True)
            emb.timestamp = datetime.datetime.utcnow()  

            await message.channel.send(embed=emb)
        except :
            await message.channel.send("There was an error in processing that redditor")
    #-----------------------------------------------------------------------Liquor???
    words = content.split()
    for word in words:
        # ends with an ending, has len 5 or more and only 25% chance
        if word.endswith(endings) and len(word) >= 5 and random.random() < 0.25:
            # HAHAHAHAHAHAHAHAHAHAH (laugh)
            await message.channel.send("{}? I barely even knew her! {}".format(word, random.choice(emotes)))
            break

client.run('')
#duccID:"287060396953698305"
'''