import discord
import random
import datetime
from zoneinfo import ZoneInfo
import json
import os
import typing
import urllib3
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
async def avatar(ctx, arg: typing.Optional[discord.Member]):
        if (arg):
            user = arg
        else:
            user = ctx.author
        embedVar = discord.Embed(title=user.name + "'s Avatar")

        embedVar.set_image(url=user.avatar.url)
        embedVar.timestamp = datetime.datetime.now(tz=ZoneInfo('Asia/Kolkata'))
        embedVar.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        
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
        

@bot.command()
async def img(ctx, subreddit):
        http = urllib3.PoolManager()
        url = "https://reddit.com/r/" + subreddit + "/top.json"
        bruh = http.request('GET', url, timeout = 2.0)
        jsonData = json.loads(bruh.data.decode('utf-8'))

        try:
            number_of_posts = jsonData['data']['dist']
        except KeyError:
            await ctx.channel.send("Too many requests, try again later")
            return

        image_posts = [];
        for i in range(0, number_of_posts):
            post_data = jsonData['data']['children'][i]['data']
            img_title = post_data['title']
            img_url = post_data['url']
            if img_url.endswith('.png') or img_url.endswith('.jpg') or img_url.endswith('.gif'):
                image_posts.append((img_title, img_url))
            elif "gallery" in img_url:
                media_id = post_data['gallery_data']['items'][0]['media_id']
                img_url = post_data['media_metadata'][media_id]['s']['u']
                img_url = img_url.replace("preview", "i", 1)
                img_url = img_url[:img_url.index('?')]
                image_posts.append((img_title, img_url))

        if (len(image_posts) == 0):
            await ctx.channel.send(f"Top posts of r/{subreddit} do not have images\n")
            return

        random_post = random.choice(image_posts)
        embedVar = discord.Embed(title=random_post[0])
        embedVar.set_image(url=random_post[1])
        embedVar.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.channel.send(embed=embedVar)


@bot.command(help="sends a random pinned message of user")
async def pinned(ctx, user : discord.Member):
    pinned_messages = await ctx.channel.pins()
    user_messages = []
    for message in pinned_messages:
        if (message.author.name == user.name and message.author.discriminator == user.discriminator):
            user_messages.append(message)

    if not user_messages:
        await ctx.channel.send("User has no pinned messages in this channel")
        return

    msgobj = random.choice(user_messages)

    embedVar = discord.Embed(title="Jump to message", description=msgobj.content, url=msgobj.jump_url)
    if msgobj.attachments:
        embedVar.set_image(url=msgobj.attachments[0].url)
    embedVar.timestamp = msgobj.created_at
    embedVar.set_footer(text=user.name, icon_url=user.avatar)

    await ctx.channel.send(embed=embedVar)


DISCORD_TOKEN = os.getenv('TOKEN')
bot.run(DISCORD_TOKEN)
