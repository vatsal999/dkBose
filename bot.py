import discord
import random
import datetime
import json
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bad_words = ["bsdk ", "gandu ", "mc ", "bc ", "randi "]

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def cuss(ctx, user):
	await ctx.channel.send(random.choice(bad_words) + user)

# command to add tag + url
@bot.command()
async def tag(ctx, arg, URL):
        # await ctx.channel.

        await ctx.channel.send(arg)

# lists all the tags available
@bot.command()
async def taglist(ctx):
        f = open('tag.json')
        taglist = json.loads(f.read())
        tag_names = ', '.join((i["tag_name"]) for i in taglist["tags"])

        embedVar = discord.Embed(title="tags",description=tag_names, color=0x1D2021)
        embedVar.timestamp = datetime.datetime.utcnow()
        embedVar.set_footer(text="use !tag <tag>")

        await ctx.channel.send(embed=embedVar)

        #await ctx.channel.send(tag_names)
        # await ctx.channel.send(taglist["tags"][i]["tag_name"])
        # await ctx.channel.send(taglist["tag_name"])
        f.close()


DISCORD_TOKEN = os.getenv('TOKEN')
bot.run(DISCORD_TOKEN)
