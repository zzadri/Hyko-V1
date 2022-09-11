import nextcord
import os
import sys

from nextcord import embeds
from nextcord import components
from nextcord.ext.commands.core import cooldown
from nextcord.types.components import ButtonStyle
import config
import random
import inspect
import main
import datetime
import aiohttp
import string
import asyncpraw
from nextcord.ext import commands
import nextcord.utils
from nextcord import Embed





# liasion avec autre fichier

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)




reddit = asyncpraw.Reddit(
  client_id="OVVBXj6_aNinv-HZqbLGag",
  client_secret="SCvEoq3wWp9j1opCd2KhMJjQpgP0cg",
  username="Hyko______",
  password="58tlRhgh3lqL0SylZusZ",
  user_agent="Hyko______"
)





class Reddits(commands.Cog, name='Reddits'):

  def __init__(self,client):
    self.client = client


# reddit


  @commands.command(aliases=['memes'])
  async def meme(self, ctx):
    subreddit = await reddit.subreddit("memes")
    all_subs = []
    top = subreddit.top(limit = 200)
    async for submission in top:
        
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = nextcord.Embed(title=name,url=f"https://reddit.com{link}", color=random.choice(config.COLORS))
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)

  @commands.command()
  async def neko(self, ctx):
    subreddit = await reddit.subreddit("nekogirls")
    all_subs = []
    top = subreddit.top(limit = 200)
    async for submission in top:
        
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = nextcord.Embed(title=name,url=f"https://reddit.com{link}", color=random.choice(config.COLORS))
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)


  @commands.command()
  async def tank(self, ctx):
    subreddit = await reddit.subreddit("TankPorn")
    all_subs = []
    top = subreddit.top(limit = 200)
    async for submission in top:
        
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = nextcord.Embed(title=name,url=f"https://reddit.com{link}", color=random.choice(config.COLORS))
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)

  @commands.command()
  async def design (self, ctx):
    subreddit = await reddit.subreddit("DesignPorn")
    all_subs = []
    top = subreddit.top(limit = 200)
    async for submission in top:
        
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = nextcord.Embed(title=name,url=f"https://reddit.com{link}", color=random.choice(config.COLORS))
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)

  @commands.command()
  async def animal (self, ctx):
    subreddit = await reddit.subreddit("Animal")
    all_subs = []
    top = subreddit.top(limit = 200)
    async for submission in top:
        
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = nextcord.Embed(title=name,url=f"https://reddit.com{link}", color=random.choice(config.COLORS))
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)

  @commands.command(aliases=['crappydesign'])
  async def crap (self, ctx):
    subreddit = await reddit.subreddit("CrappyDesign")
    all_subs = []
    top = subreddit.top(limit = 200)
    async for submission in top:
        
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = nextcord.Embed(title=name,url=f"https://reddit.com{link}", color=random.choice(config.COLORS))
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)

  @commands.command(aliases=['Warship'])
  async def warship (self, ctx):
    subreddit = await reddit.subreddit("WarshipPorn")
    all_subs = []
    top = subreddit.top(limit = 200)
    async for submission in top:
        
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = nextcord.Embed(title=name,url=f"https://reddit.com{link}", color=random.choice(config.COLORS))
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)

  @commands.command(aliases=['Warship'])
  async def warship (self, ctx):
    subreddit = await reddit.subreddit("WarshipPorn")
    all_subs = []
    top = subreddit.top(limit = 200)
    async for submission in top:
        
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = nextcord.Embed(title=name,url=f"https://reddit.com{link}", color=random.choice(config.COLORS))
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)

  @commands.command(aliases=['satisfyingasfuck'])
  async def satisfying (self, ctx):
    subreddit = await reddit.subreddit("satisfyingasfuck")
    all_subs = []
    top = subreddit.top(limit = 200)
    async for submission in top:
        
      all_subs.append(submission)
      
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = nextcord.Embed(title=name,url=f"https://reddit.com{link}", color=random.choice(config.COLORS))
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)



def setup(client):
  client.add_cog(Reddits(client))
  print("Reddit Cog is load")