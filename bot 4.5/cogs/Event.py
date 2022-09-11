import nextcord
import os
import sys
import json
from nextcord import client
from nextcord import member
from nextcord import emoji
from nextcord import Embed
from nextcord import embeds
from nextcord.message import Message
import config
import asyncio
import random
import inspect
import nextcord.utils
from nextcord.ext import commands, tasks
import datetime

# liasion avec autre fichier

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)




class event(commands.Cog, name='event'):

  def __init__(self,client):
    self.client = client


  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = nextcord.utils.get(member.guild.text_channels, name="🚀𝐀𝐞𝐫𝐨𝐩𝐨𝐫𝐭")
    if channel:
      embed = nextcord.Embed(description=f"Bienvenue sur le serveur {member.mention} !",color=random.choice(config.COLORS))
      embed.set_thumbnail(url=member.avatar)
      embed.set_author(name=member.name, icon_url=member.avatar)
      embed.timestamp = datetime.datetime.utcnow()
      
      await channel.send(embed=embed)

    role = nextcord.utils.get(member.guild.roles, name=config.ROLE_NAME)
    await member.add_roles(role)


#sys log

  #@commands.Cog.listener()
  #async def on_message_delete(self, member, message):
  #  channel = self.client.get_channel(int(config.MOD_ID))
  #  embed = nextcord.Embed(title="Message supprimé")
  #  embed.add_field(name="ㅤ", value=f"message: {message.content} by {message.author} was deleted in {message.channel}", inline=False)
  #  embed.set_author(name=member.name, icon_url=member.avatar)
  #  embed.timestamp = datetime.datetime.utcnow()

  #  await channel.send(embed=embed)










  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      embed=nextcord.Embed(title="**Erreur**", description="Cette commande n'existe pas !", color=config.ERROR_COLOR)
      embed.set_author(name="Hyko", url="https://discord.com/invite/BVpNgUxRZ2", icon_url="https://cdn.discordapp.com/avatars/552174858985799680/846123c387918e619c9f8e3d983f1da1.png")
      embed.set_thumbnail(url="https://img.icons8.com/ios/452/database-error.png")
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingRequiredArgument):
      embed=nextcord.Embed(title="**Erreur**", description="Il manque un argument.", color=config.ERROR_COLOR)
      embed.set_author(name="Hyko", url="https://discord.com/invite/BVpNgUxRZ2", icon_url="https://cdn.discordapp.com/avatars/552174858985799680/846123c387918e619c9f8e3d983f1da1.png")
      embed.set_thumbnail(url="https://img.icons8.com/ios/452/database-error.png")
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
      embed=nextcord.Embed(title="**Erreur**", description="Vous n'avez pas les permissions pour faire cette commande.", color=config.ERROR_COLOR)
      embed.set_author(name="Hyko", url="https://discord.com/invite/BVpNgUxRZ2", icon_url="https://cdn.discordapp.com/avatars/552174858985799680/846123c387918e619c9f8e3d983f1da1.png")
      embed.set_thumbnail(url="https://img.icons8.com/ios/452/database-error.png")
      await ctx.send(embed=embed)

    elif isinstance(error, commands.CheckFailure):
      embed=nextcord.Embed(title="**Erreur**", description="Oups vous ne pouvez utilisez cette commande.", color=config.ERROR_COLOR)
      embed.set_author(name="Hyko", url="https://discord.com/invite/BVpNgUxRZ2", icon_url="https://cdn.discordapp.com/avatars/552174858985799680/846123c387918e619c9f8e3d983f1da1.png")
      embed.set_thumbnail(url="https://img.icons8.com/ios/452/database-error.png")
      await ctx.send(embed=embed)


    elif isinstance(error.original, nextcord.Forbidden):
      embed=nextcord.Embed(title="**Erreur**", description="Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande", color=config.ERROR_COLOR)
      embed.set_author(name="Hyko", url="https://discord.com/invite/BVpNgUxRZ2", icon_url="https://cdn.discordapp.com/avatars/552174858985799680/846123c387918e619c9f8e3d983f1da1.png")
      embed.set_thumbnail(url="https://img.icons8.com/ios/452/database-error.png")
      await ctx.send(embed=embed)





def setup(client):
  client.add_cog(event(client))
  print("event Cog is load")