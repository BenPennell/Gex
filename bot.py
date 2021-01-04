import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 287060396953698305:
        client.load_extension(f'cogs.{extension}')
        await ctx.send("loaded {}".format(extension))
    else:
        await ctx.send("YOU'RE NOT ALLOWED TO DO THAT :(")

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 287060396953698305:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send("unloaded {}".format(extension))
    else:
        await ctx.send("YOU'RE NOT ALLOWED TO DO THAT :(")

@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 287060396953698305:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send("reloaded {}".format(extension))
    else:
        await ctx.send("YOU'RE NOT ALLOWED TO DO THAT :(")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('YOUR TOKEN HERE')
#duccID:"287060396953698305"