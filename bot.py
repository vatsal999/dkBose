import discord
import random
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
        for i in taglist["tags"]:
            await ctx.channel.send(i["tag_name"])
        # await ctx.channel.send(taglist["tags"][i]["tag_name"])
        # await ctx.channel.send(taglist["tag_name"])
        f.close()





DISCORD_TOKEN = os.getenv('TOKEN')
bot.run(DISCORD_TOKEN)
