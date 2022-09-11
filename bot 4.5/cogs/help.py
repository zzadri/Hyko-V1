import nextcord
import os
import sys
import json
from nextcord import client
from nextcord import embeds
from nextcord.member import Member
import nextcord.utils
import config
import asyncio
import random
from nextcord import Embed
import inspect
from nextcord.ext import commands
import datetime

# liasion avec autre fichier

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)



class help(commands.Cog, name='help'):

  def __init__(self,client):
    self.client = client


  @commands.command()
  async def help(self, ctx, arg=None):
    await ctx.message.delete()
    if arg == None:
      reglesembed= nextcord.Embed(title="__**Help**__",description="ㅤ", color=random.choice(config.COLORS))
      reglesembed.set_thumbnail(url="https://cdn.nextcordapp.com/attachments/719960352028360796/883728286805536778/38177.png")
      reglesembed.add_field(name="Catégorie: Fun", value="`*avatar`\nla commande Avatar permet d'afficher votre avatar ou celui de quelqu'un d'autre", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*eihtball | 8b | 8ball | m8b`\nposer une question avec cette commande et le destin vous repondra", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*rdmimg`\ncette commande envoie une image random", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*rdmvid`\ncette commande envoie une vidéo random", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*rdmcit`\ncette commande envoie une citation random", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*serverinfo`\ncette commande affiche des informations sur le serveur", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*version`\ncette commande affiche des informations sur le bot", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*userinfo`\ncette commande affiche des informations sur l'utilisateur souhaité", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*lc | lovecalc`\ncette commande affiche votre score d'amour entre toi et quelqu'un d'autre", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*meme`\ncette commande affiche un meme aléatoire du sub reddit r/memes", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*math`\ncette commande a les fonction d'une calculatrice", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*counter`\ncette commande fait apparaitre un conteur essayer d'arrivé au bout !", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*morpion`\nune petite partie de morpion ?", inline=False)
      reglesembed.add_field(name="ㅤ",value="`*google`\nfait une recherche avec cette commande !", inline=False)


      reglesembed2= nextcord.Embed(color=random.choice(config.COLORS))
      reglesembed2.add_field(name="Catégorie: Moderation", value="`*regles`\nla commande regles permet d'afficher des régles déjà écrite", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*mute`\nla commande mute permet de mute une personne", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*unmute`\nla commande unmute permet de redonnée la permision de parlé a une personne mute", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*ban`\nla commande ban permet de ban une personne", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*kick`\nla commande ban permet de kick une personne", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*pardon`\nla commande pardon permet de unban une personne", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*clear`\nla commande clear permet d'effacer un nombre de message", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*config`\nla commande config permet de rajouté toute les foncionalité que le bot a besoin pour bien fonctione", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*warn`\nla commande warn sert a warn une personne", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*setprefix`\nla commande setprefix change le prefix du bot", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*slowmode`\nla commande slowmode permet d'acctivé le slowmode dans un salon textuel", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*gcreate`\nla commande gcreate permet de crée un giveaway", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*lock`\nla commande lock permet de fermer un salon textuel", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*unlock`\nla commande unlock permet de re-ouvrir un salon textuel", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*move`\nla commande move permet de move une personne dans un salon spécifique", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*stats`\nla commande stats permet de voire certaine statistique du bot en temps réelle", inline=False)
      reglesembed2.add_field(name="ㅤ",value="`*say`\nla commande say permet de faire parler le bot avec une phrase donnée", inline=False)
      

      reglesembed3= nextcord.Embed(color=random.choice(config.COLORS))
      reglesembed3.add_field(name="Catégorie: Musique", value="`*play`\nsuivie d'un lien youtube le bot ce connectera a votre salon pour jouer le son de cette musique. si une musqiue est déjà jouer la musique ce mettera directement dans une fil d'attente", inline=False)
      reglesembed3.add_field(name="ㅤ",value="`*leave`\npermet de faire leave le bot du salon ou il est connecter", inline=False)
      reglesembed3.add_field(name="ㅤ",value="`*skip`\nla commande skip permet de changer la musique et passe directement a la prochaine", inline=False)
      reglesembed3.add_field(name="ㅤ",value="`*pause`\nla commande pause permet d'arreter la musique", inline=False)
      reglesembed3.add_field(name="ㅤ",value="`*resume`\nla commande resume permet de reprendre la musique", inline=False)
      reglesembed3.set_footer(text=f'Requested by - {ctx.author}',icon_url=ctx.author.avatar)
      await ctx.author.send(embed=reglesembed)
      await ctx.author.send(embed=reglesembed2)
      await ctx.author.send(embed=reglesembed3)
    



    elif arg == "avatar":
      embedavatar= nextcord.Embed(title="**Help *avatar**", color=random.choice(config.COLORS))
      embedavatar.set_thumbnail(url="https://cdn.discordapp.com/attachments/722842924345458709/896070466073149500/book.png")
      embedavatar.add_field(name="ㅤ" , value="Pour executé la commande avatar vous pouvez écrire, \n`*avatar` pour avoir votre avatar \n`*avatar @Alaix#3630` pour avoir celui de quelqu'un d'autre", inline=False)
      embedavatar.set_footer(text=f'Requested by - {ctx.author}',icon_url=ctx.author.avatar)

      await ctx.author.send(embed=embedavatar)
      



    elif arg == "eihtball" or "8b" or "8ball" or "m8b":
      embedeihtball= nextcord.Embed(title="**Help *eihtball**", color=random.choice(config.COLORS))
      embedeihtball.set_thumbnail(url="https://cdn.discordapp.com/attachments/722842924345458709/896070466073149500/book.png")
      embedeihtball.add_field(name="ㅤ" , value="Pour executé la commande eihtball vous pouvez écrire, \n`*eihtball | 8b | 8ball | m8b [message]", inline=False)
      embedeihtball.set_footer(text=f'Requested by - {ctx.author}',icon_url=ctx.author.avatar)

      await ctx.author.send(embed=embedeihtball)

    elif arg == "rdmimg":
      embedrdmimg= nextcord.Embed(title="**Help *rdmimg**", color=random.choice(config.COLORS))
      embedrdmimg.set_thumbnail(url="https://cdn.discordapp.com/attachments/722842924345458709/896070466073149500/book.png")
      embedrdmimg.add_field(name="ㅤ" , value="Pour executé la commande rdmimg vous pouvez écrire, \n`*rdmimg", inline=False)
      embedrdmimg.set_footer(text=f'Requested by - {ctx.author}',icon_url=ctx.author.avatar)

      await ctx.author.send(embed=embedrdmimg)

    elif arg == "rdmcit":
      embedrdmcit= nextcord.Embed(title="**Help *rdmcit**", color=random.choice(config.COLORS))
      embedrdmcit.set_thumbnail(url="https://cdn.discordapp.com/attachments/722842924345458709/896070466073149500/book.png")
      embedrdmcit.add_field(name="ㅤ" , value="Pour executé la commande rdmcit vous pouvez écrire, \n`*rdmcit", inline=False)
      embedrdmcit.set_footer(text=f'Requested by - {ctx.author}',icon_url=ctx.author.avatar)

      await ctx.author.send(embed=embedrdmcit)





def setup(client):
  client.add_cog(help(client))
  print("help Cog is load")