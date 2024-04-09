import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests
import random
import json

load_dotenv(dotenv_path="config")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def quote(ctx):
    response = requests.get('https://dummyjson.com/products')
    data = response.json()
    product_choice = random.choice(data.get('products'))
    await ctx.send(product_choice.get('description', None))


@bot.command()
async def challenge(ctx):
    with open('challenges.json', 'r') as file:
        data = json.load(file)
    challenge_choice = random.choice(data.get('challenges'))
    await ctx.send(f"{challenge_choice.get('name', None)} : {challenge_choice.get('url', None)}")


@bot.command()
async def list(ctx):
    with open('challenges.json', 'r') as file:
        data = json.load(file)
    
    all_challenges = data.get('challenges')
    list_challenges = [f"{challenge.get('name', None)} : {challenge.get('url', None)}"
                      for challenge in all_challenges]
    await ctx.send('\n'.join(list_challenges))

bot.run(os.getenv("TOKEN"))