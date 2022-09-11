from typing import TypedDict
import nextcord
import os
import main
import sys
import inspect
import json
import asyncio
import io
import csv
import random
import logging
import discord
from nextcord import embeds
import psutil
import aiohttp
from nextcord.channel import CategoryChannel
from nextcord.ext import commands, tasks
from time import ctime
import nextcord.utils
from nextcord import Embed
from nextcord import client

from main import get_prefix, uptimeCounter






# liasion avec autre fichier

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import config








class Mod(commands.Cog, name='Moderation'):

  def __init__(self,client):
    self.client = client















  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def regles(self, ctx):
    await ctx.message.delete()
    reglesembed= nextcord.Embed(title="__**Règlement du nextcord**__", description= "__**Règle n°1:**__\n\nLe respect très important dans la vie, c'est même la valeur n°1, alors pas d'insulte, de propos racistes, sexistes, ou encore homophobes. Bien sur pas de harcèlement, c'est condamnable !\n\n__**Règle n°2:**__\n\nÉvitez les photo de profil / pseudo inappropriés, pas de pornographie !\n\n__**Règle n°3:**__\n\nPas de spam / flood, ou alors abus de majuscules, ça gène les autres et ça vous ferait chier vous même !\n\n__**Règle n°4:**__\n\nN'essayez pas faire votre pub, seules les personnes de l'entourage des adminsistrateur et qu'il soutien pourront à quelques reprises la faire.\n\n__**Règle n°5:**__\n\nInterdit de @ sans arrêt un modo ou encore moins le owner directement, aucun intérêt, il voit vos messages, si il ne répond pas directement c'est qu'il est occupé.\n\n__**Règle n°6:**__\n\nEssayez vraiment de respecter les différents channels et leur contenu, on ne parle pas de n'importe quoi n'importe où.\n\n__**Règle n°7:**__\n\nSPOILER interdits sans la commande /spoiler !!! ||Ceci est un exemple||", color=config.SUCCESS_COLOR)
    reglesembed.set_footer(text= "Si ces règles ne sont appliquées, des sanctions seront à prévoir, et pire, une exclusion ou un bannissement sont vite arrivés, alors soyez sages 😁")
    reglesembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/719960352028360796/883728286805536778/38177.png")

    await ctx.send(embed = reglesembed)




# mute
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def mute(self, ctx, member : nextcord.Member,*, reason="None"):
      guild = ctx.guild
      mutedRole = nextcord.utils.get(guild.roles, name="Muted")

      if not mutedRole:
          await guild.create_role(name="Muted")

      if member == ctx.author:
          await ctx.send("Vous ne pouvez pas vous mute.")

          for channel in guild.channels:
              await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
      muteembed = nextcord.Embed(title="Mute", description=f"{member.mention} à été mute ", colour=nextcord.Colour.light_gray())
      muteembed.add_field(name="reason:", value=reason, inline=False)
      await ctx.send(embed=muteembed)
      await member.add_roles(mutedRole, reason=reason)
      mutedembed = nextcord.Embed(title="Vous avez été mute", description=f"{member.mention} à été mute du serveur {guild.name}", colour=config.WARNING_COLOR)
      mutedembed.add_field(name="reason:", value=reason, inline=False)
      await ctx.send(embed=muteembed)
      await member.send(embed= mutedembed)








#unmute
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def unmute(self, ctx, member : nextcord.Member,*, reason="None"):
      guild = ctx.guild
      mutedRole = nextcord.utils.get(guild.roles, name="Muted")
      embed = nextcord.Embed(title="Un-Mute", description=f"{member.mention} à été un-mute ", colour=config.WARNING_COLOR)
      embed.add_field(name="reason:", value=reason, inline=False)
      await ctx.send(embed=embed)
      await member.remove_roles(mutedRole, reason=reason)
      unmutedembed = nextcord.Embed(title="Vous avez été un-mute", description=f"{member.mention} à été un-mute du serveur {guild.name}", colour=config.WARNING_COLOR)
      unmutedembed.add_field(name="reason:", value=reason, inline=False)
      await member.send(embed=unmutedembed)









#kick
  @commands.command(aliases=['kicked'])
  @commands.has_permissions(kick_members = True)
  async def kick(self, ctx, member:nextcord.Member, *, reason=None):
    await member.kick(reason=reason)


    memberAvatar = member.avatar_url

    kickEmbed = nextcord.Embed(title = f"{member.name} a été kick", description=f'**{member.mention}** à bien été kick', color=config.WARNING_COLOR)
    kickEmbed.set_thumbnail(url = memberAvatar)

    await ctx.send(embed = kickEmbed)









# ban
  @commands.command(aliases=['banned'])
  @commands.has_permissions(ban_members = True)
  async def ban(self, ctx, member:nextcord.Member, *, reason=None):
    await member.ban(reason=reason)

    memberAvatar = member.avatar_url

    banEmbed = nextcord.Embed(title = f"{member.name} a été ban", description=f'**{member.mention}** à bien été bannis', color=config.WARNING_COLOR)
    banEmbed.set_thumbnail(url = memberAvatar)


    await ctx.send(embed = banEmbed)









# unban
  @commands.command(aliases=['pardon'])
  @commands.has_permissions(ban_members = True)
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user

      if(user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)

        unbanEmbed = nextcord.Embed(title = "Le joueur a été unban", description=f'Le joueur que vous avez choisi a été unban', color=config.WARNING_COLOR)
        unbanEmbed.set_thumbnail(url = "https://img.icons8.com/ios/50/000000/escape.png")

        await ctx.send(embed = unbanEmbed)
        return










# clear
  @commands.command(aliases=['purge'])
  @commands.has_permissions(manage_messages = True)
  async def clear(self, ctx, amount=12):
    ammount = amount+2
    if amount > 102:
      await ctx.send('tu ne peux supprimé plus de 100 messages')
    else:
      await ctx.channel.purge(limit=amount)

      clearembed = nextcord.Embed(title = "**message supprimé**", description=f'des messages on été supprimé', color=config.WARNING_COLOR)
      clearembed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/719960352028360796/883726232414453830/3370093.png")

      await ctx.send(embed = clearembed)















# say
  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def say(self, ctx, number, *texte):
    for i in range(int(number)):
      await ctx.send(" ".join(texte))


# config
  @commands.command(aliases= ['config'])
  @commands.has_permissions(manage_messages = True)
  async def configuration(self, ctx):
    guild = ctx.guild
    mutedRole = nextcord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
      await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    if not channel.name == "log":
      await ctx.guild.create_text_channel(name="log")
      await asyncio.sleep(3)
      for channel in guild.channels:
        await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)


    configembed= nextcord.Embed(title="**Configuration**", description= "La configuration du bot est fini !", color=config.SUCCESS_COLOR)
    configembed.set_thumbnail(url="https://img.icons8.com/ios/50/000000/accept-database.png")

    await ctx.send(embed = configembed)










# Prefix perso
  @commands.command(aliases=['prefix'])
  @commands.has_permissions(manage_channels = True)
  async def setprefix(self, ctx, prefixset = None):

    if (prefixset == None):
      prefixset = '*'

    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefixset

    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)
    

    prembed=nextcord.Embed(title="**Info**", description=f'Modification au niveau du bot. le prefix est maintenant : ``{prefixset}``', color=config.INFO_COLOR)
    prembed.set_thumbnail(url="https://img.icons8.com/ios/50/000000/edit--v4.png")
    prembed.set_author(name="Hyko", url="https://discord.com/invite/BVpNgUxRZ2", icon_url="https://cdn.discordapp.com/attachments/722842924345458709/826128582476562503/avatar.png")
    await ctx.send(embed=prembed)

#info

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def stats(self, ctx):
    global ts, tm, th, td
    embed = nextcord.Embed(title="Mes stats !", color=config.INFO_COLOR)
    embed.add_field(name="Heures:", value=main.td, inline=True)
    embed.add_field(name="Minutes:", value=main.th, inline=True)
    embed.add_field(name="seconde:", value=main.tm, inline=True)
    embed.add_field(name="milliseconde:", value=main.ts, inline=True)
    embed.add_field(name="CPU", value=f"{psutil.cpu_percent()}%", inline=True)
    embed.add_field(name="RAM", value=f"{psutil.virtual_memory()[2]}%", inline=True)
    await ctx.send(embed = embed)




#slowmode

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def slowmode(self, ctx, time:int):
    if time == 0:
      slowdembed = nextcord.Embed(title="**Info**", description=f"Slowmode désactivé", color=config.INFO_COLOR)
      await ctx.send(embed=slowdembed)
      await ctx.channel.edit(slowmode_delay = 0)
    elif time > 21600:
      sembed=nextcord.Embed(title="**Erreur**", description="vous ne pouvez pas activé un slowmode de plus de 6 heures", color=config.ERROR_COLOR)
      sembed.set_author(name="Hyko", url="https://discord.com/invite/BVpNgUxRZ2", icon_url="https://cdn.discordapp.com/attachments/722842924345458709/826128582476562503/avatar.png")
      sembed.set_thumbnail(url="https://img.icons8.com/ios/452/database-error.png")
      await ctx.send(embed=sembed)
      return
    else:
      await ctx.channel.edit(slowmode_delay = time)
      slowembed = nextcord.Embed(title="**Info**", description=f"Slowmode mis a {time}s", color=config.INFO_COLOR)
      await ctx.send(embed=slowembed)



#channelmute


  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def lock(self, ctx, raison=None):
    await ctx.message.delete()

    channel = self.client.get_channel(int(config.MOD_ID))
    guild = ctx.guild
    lock = nextcord.utils.get(guild.roles, name=config.ROLE_NAME)


    await ctx.channel.set_permissions(lock, send_messages=False, read_messages=True)


    embed=nextcord.Embed(title="**Lock**", description="Le salon textuel a été fermé par un modérateur.", color=config.ERROR_COLOR)
    embed.set_thumbnail(url="https://img.icons8.com/ios/50/000000/lock--v1.png")

    embedVar = nextcord.Embed(title="Salon Lock", color=config.INFO_COLOR)
    embedVar.set_thumbnail(url="https://img.icons8.com/ios/50/000000/lock--v1.png")
    embedVar.add_field(name="Modérateur:", value=f"**{ctx.author}**", inline=False)
    embedVar.add_field(name="Salon:", value=f"**{ctx.channel.mention}**", inline=False)
    embedVar.add_field(name="Time:", value=f"**{ctime()}**", inline=False)
    embedVar.add_field(name="raison:", value=f"**{raison}**", inline=False)
    await channel.send(embed=embedVar)

    await ctx.send(embed=embed)






  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def unlock(self, ctx):
    await ctx.message.delete()

    channel = self.client.get_channel(int(config.MOD_ID))
    guild = ctx.guild
    lock = nextcord.utils.get(guild.roles, name=config.ROLE_NAME)
    


    await ctx.channel.set_permissions(lock, send_messages=None, read_messages=None)

    embed=nextcord.Embed(title="**UnLock**", description="Le salon textuel a été re-ouvert par un modérateur.", color=config.SUCCESS_COLOR)
    embed.set_thumbnail(url="https://img.icons8.com/ios/50/000000/unlock.png")


    embedVar = nextcord.Embed(title="Salon UnLock", color=config.INFO_COLOR)
    embedVar.set_thumbnail(url="https://img.icons8.com/ios/50/000000/unlock.png")
    embedVar.add_field(name="Modérateur:", value=f"**{ctx.author}**", inline=False)
    embedVar.add_field(name="Salon:", value=f"**{ctx.channel.mention}**", inline=False)
    embedVar.add_field(name="Time:", value=f"**{ctime()}**", inline=False)
    await channel.send(embed=embedVar)

    await ctx.send(embed=embed)

#move

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def move(self, ctx, member : nextcord.Member, channel : nextcord.VoiceChannel):
    if member == None:
      await ctx.send("Vous devez spécifier un membre.")

    if channel == None:
      await ctx.send("Vous devez spécifier un salon.")
    else:
      await member.move_to(channel)






# Warn 
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def warn(self, ctx, member : nextcord.Member,*,reason="None", message):
    channel = self.client.get_channel(int(config.MOD_ID))

    if member == ctx.author:
      await ctx.send("Vous ne pouvez pas vous avertir.")

    else:
      em = nextcord.Embed(title="**Warned**", color=nextcord.Color.red())
      em.add_field(name="Modérateur:", value=f"**{ctx.author}**", inline=False)
      em.add_field(name="Salon:", value=f"**{ctx.channel.mention}**", inline=False)
      em.add_field(name="Membre", value=f"**{member}**", inline=False)
      em.add_field(name="Time:", value=f"**{ctime()}**", inline=False)
      em.add_field(name="raison:", value=f"**{reason}**", inline=False)

      em2 = nextcord.Embed(title="**Warned**", description=f"Vous avez été warn car : {reason}", color=nextcord.Color.red())
      await member.send(embed=em2)
      await channel.send(embed=em)












def setup(client):
  client.add_cog(Mod(client))
  print("Mod Cog is load")