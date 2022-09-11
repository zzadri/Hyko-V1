import nextcord
import os
import asyncio
import sys
import config
import inspect
import random
from nextcord import client
import nextcord.utils
from nextcord import Embed
import json
from nextcord.ext import commands





# liasion avec autre fichier

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)




class Give(commands.Cog, name='Giveaway'):

  def __init__(self,client):
    self.client = client


  # giveaway sys

  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def gcreate(self, ctx, time=None, *, prize=None):
    if time == None:
      return await ctx.send("Merci d'inclure un temps !")
    elif prize == None:
      return await ctx.send(f"Merci d'inclure un prix ! exemple : <gcreate> <temps> <prix>")
    embed = nextcord.Embed(title='Nouveau Giveaway!', description=f'{ctx.author.mention} vous donne **{prize}**')
    time_convert = {"s":1, "m":60, "h":3600, "d": 86400} 
    gawtime = int(time[0]) * time_convert[time[-1]]
    embed.set_footer(text=f'Le Giveaway se fini dans {time}')
    gaw_msg = await ctx.send(embed = embed)

    await gaw_msg.add_reaction("🎉")
    await asyncio.sleep(gawtime)

    new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

    users = await new_gaw_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"YYYYAAAAAY !!! {winner.mention} est le gagnant du Giveaway il remporte **{prize}**")


def setup(client):
  client.add_cog(Give(client))
  print("Giveaway Cog is load")