import discord
import random
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

@bot.command()
async def tag(ctx, tag)
    await ctx.channel.send


DISCORD_TOKEN = os.getenv('TOKEN')
bot.run(DISCORD_TOKEN)
