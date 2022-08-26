import discord
import random
import datetime
from zoneinfo import ZoneInfo
import json
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bad_words = ["bsdk ", "gandu ", "mc ", "bc ", "randi "]

command_prefix = "bsdk "
bot = commands.Bot(command_prefix , intents=intents)


@bot.command()
async def cuss(ctx, *, user):
	await ctx.channel.send(random.choice(bad_words) + user)


# command to add tag + url
# async def tag(ctx, arg, msgID):
# @bot.command()
# async def tag(ctx, arg):
#         # await ctx.channel
#         # fetch_message(id)
#         if arg == "view":
#             f = open('tag.json')
#             taglist = json.loads(f.read())
#             for i in taglist["tags"]["tag_name"]:
#                 print(taglist[i])
#             f.close()
#         elif arg == "add":



@bot.command(help="Displays user avatar")
async def avatar(ctx):
        embedVar = discord.Embed(title=ctx.author.name + "'s Avatar")

        embedVar.set_image(url=ctx.author.avatar.url)
        embedVar.timestamp = datetime.datetime.now(tz=ZoneInfo('Asia/Kolkata'))
        embedVar.set_footer(text="Requested by " + ctx.author.name)
        
        await ctx.channel.send(embed=embedVar)
    

# lists all the tags available
@bot.command(help='lists all tags available for !tag <tagname>')
async def taglist(ctx):
        f = open('tag.json')
        taglist = json.loads(f.read())
        tag_names = ', '.join((i["tag_name"]) for i in taglist["tags"])

        embedVar = discord.Embed(title="tags",description=tag_names, color=0x1D2021)
        embedVar.timestamp = datetime.datetime.utcnow()

        embedVar.set_footer(text=f"use: {command_prefix}tag <tag>")

        await ctx.channel.send(embed=embedVar)

        #await ctx.channel.send(tag_names)
        # await ctx.channel.send(taglist["tags"][i]["tag_name"])
        # await ctx.channel.send(taglist["tag_name"])
        f.close()

@bot.command(help=f"quotes a msg. usage: {command_prefix}quote <msgID>")
async def quote(ctx, msgID):
        msgobj = await ctx.fetch_message(msgID)
        msg = msgobj.content

        embedVar = discord.Embed(title=msgobj.author, description=msg, url=msgobj.jump_url)
        embedVar.set_thumbnail(url=msgobj.author.avatar.url)
        embedVar.timestamp = msgobj.created_at

        await ctx.channel.send(embed=embedVar)

        

#@bot.command(name="rimg")
#sync def reddit_img(ctx, subreddit):
#await bot.process_commands(message)
        

DISCORD_TOKEN = os.getenv('TOKEN')
bot.run(DISCORD_TOKEN)
