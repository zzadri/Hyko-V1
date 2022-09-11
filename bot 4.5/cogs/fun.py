from io import BytesIO
import nextcord
import os
import sys

from nextcord import embeds
from nextcord import components
from nextcord.ext.commands.core import cooldown
from nextcord.types.components import ButtonStyle
from twitchAPI.twitch import Twitch
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


NUMBER_LIST = ["1%","2%","3%","4%","5%","6%","7%","8%","9%","10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%","31%","32%","33%","34%","35%","36%","37%","38%","39%","40%","50%","51%","52%","53%","54%","55%","56%","57%","58%","59%","60%","61%","62%","63%","64%","65%","66%","67%","68%","69%","70%","71%","72%","73%","74%","75%","76%","77%","78%","79%","80%","81%","82%","83%","84%","85%","86%","87%","88%","89%","90%","91%","92%","93%","94%","95%","96%","97%","98%","99%","100%","667% __**EKIP**__", "**ထ**%"]




class Fun(commands.Cog, name='Fun'):

  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['p'])
  async def ping(self, ctx):
    await ctx.send('pong!')




# reddit


  @commands.command(aliases=['lovecalc'])
  async def lc(self, ctx, member : nextcord.Member = None):
    if member == None:
      member = ctx.author

    lcembed = Embed(title = f"{ctx.author.name} + {member.name}",description=  f"votre score d'amour est de = {random.choice(NUMBER_LIST)} :two_hearts:", color=config.MAIN_COLOR)

    await ctx.send(embed = lcembed)




  @commands.command()
  async def avatar(self, args ,ctx, member : nextcord.Member = None):
    if args == None:
      if member == None:
        member = ctx.author

      memberAvatar = member.avatar

      avaEmbed = Embed(title = f"{member.name}'s Avatar", color=config.MAIN_COLOR)
      avaEmbed.set_image(url = memberAvatar)

      await ctx.send(embed = avaEmbed)



  @commands.command(aliases=['8ball', '8b', 'm8b'])
  async def eihtball(self, ctx, *, question):
    response_list = [
    "je pense, oui", 
    "oui", 
    "non", 
    "Essaye plus tard", 
    "Essaye encore", 
    "peut-être", 
    "Très peu probable", 
    "Pas d'avis", 
    "C'est ton destin", 
    "D'après moi oui", 
    "C'est certain", 
    "Oui absolument", 
    "Tu peux compter dessus", 
    "Peu probable", 
    "Faut pas rêver", 
    "N'y compte pas", 
    "Impossible", 
    "Très probable", 
    "C'est bien parti"]

    huitballembed= nextcord.Embed(title = f":8ball: Question: {question}", description=  f"{random.choice(response_list)}", color=config.MAIN_COLOR)
    huitballembed.set_thumbnail(url="https://img.icons8.com/ios/50/000000/bowling-ball.png")

    await ctx.send(embed = huitballembed)
  


  @commands.command()
  async def rdmimg(self, ctx):
    img_list = [
    "https://cdn.discordapp.com/attachments/824769408257622057/828902003706167326/animals.png",
    "https://cdn.discordapp.com/attachments/824024512118653001/826216030585880646/2021-03-30_00.07.12.png",
    "https://cdn.discordapp.com/attachments/824768629631221770/825694107942912000/20210327_182506.jpg",
    "https://cdn.discordapp.com/attachments/824768629631221770/825693933911801866/Snapchat-623037135.jpg",
    "https://media.discordapp.net/attachments/614747828853407745/617271655835893760/image0.png",
    "https://cdn.discordapp.com/attachments/824768629631221770/825496389017665536/Screenshot_20210326_122638.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883311227806306344/EjY5d8RWkAAKJqT.png",
    "https://cdn.discordapp.com/attachments/719960352028360796/883312147638149170/Z.png",
    "https://cdn.discordapp.com/attachments/719960352028360796/883315220351688724/unknown.png",
    "https://cdn.discordapp.com/attachments/719960352028360796/883317765811871764/unknown.png",
    "https://cdn.discordapp.com/attachments/824034311371096115/835834120076525588/unknown.png",
    "https://cdn.discordapp.com/attachments/824034311371096115/834705582811512882/EicA-T2WAAEViQc.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883324594876977152/grg.jpg",
    "https://pbs.twimg.com/media/ExqpaX-XIAw5SCt.jpg:large",
    "https://cdn.discordapp.com/attachments/719960352028360796/883632875302432808/54654.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883633235194687498/65465.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883633296993570886/94535.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883633365725642772/654465.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883633455630516264/654654.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883633557413720114/698535.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883633648279093248/984654.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883633779497902090/2465464.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883633857688125470/4476465.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883633920455897098/5264654.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883633980841263164/47641657.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634030732521512/54652695.PNG",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634082943221780/65465465.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634146667278356/89465454.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634191730876476/221168825_225833319397383_31265394272092552_n.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634299084095508/227763160_884598168798954_1858918127757817575_n.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634460061487134/234500260_506113547146844_696467689214211648_n.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634515501801492/236463248_4281057845293208_7597036714729433184_n.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634564302512138/240411177_1086204008577508_6543271759175753760_n.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634686243516446/240637160_541991013796131_8784269181372762679_n.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634735950209094/240855940_1160642421108883_5650661139743949931_n.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634885137403934/564765487.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883634968327233587/689465465.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635018562408458/987465465.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635085235089448/4465446546.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635142281814016/6546549684.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635199097856000/6554635498.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635247655313448/7897458747.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635312046256138/gerged.jpg",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635355239198750/rgedr.jpg",]
    
    rdmimgembed= nextcord.Embed(title = "**image random**")
    rdmimgembed.set_image(url=f"{random.choice(img_list)}")

    await ctx.send(embed = rdmimgembed)

  @commands.command()
  async def rdmcit(self, ctx):
    cit_list = [
    "Il est plus facile de conseiller que de faire",
    "Les grands diseurs ne sont pas les grands faiseurs",
    "Toutes des putes sauf maman. - Socrate",
    "Qui vend au public quelque talent de sa femme s'expose à tout livrer. - Fafin",
    "Avoir des imitateurs ridicules, c'est l'inévitable rançon du génie. - Fafin",
    "J'ai ramassé un caillou, il était dur. - Darkmariosan",
    "La saveur du talent et du mérite n'échappe qu'à ceux qui en sont démunis. - Fafin",
    "Avoir des imitateurs ridicules, c'est l'inévitable rançon du génie. - Fafin",
    "Une envie de soulever vos mères tel le vent souffle le mat d'un bateau. - Force55",
    "si je dit un truc vous allez répliquez que je suis parano - Monsieur Debouis",
    "On se protège des autres au lieu de se protéger de soi-même.",
    "l'avis des autres n'est que la vie des autres",
    "Ne laisse jamais les autres te dicter tes envies. - zzAdri",
    "Je connais mes limites c'est pourquoi je vais au-delà",
    "L'échec n'est qu'une opportunité pour recommencer la même chose plus intelligement",
    "Les mots peuvent dire beaucoup, les regards disent tous",
    "ne laisse pas le comportement des autres détruire ta paix intérieure.",
    "Ne soit pas triste pour une personne qui t'a laisser tomber. soit triste pour elle, car elle vien de perdre quelqu'un de ✨magique✨"]
    
    rdmcitembed= nextcord.Embed(title = "**citation random**", description= f"*{random.choice(cit_list)}*")

    await ctx.send(embed = rdmcitembed)


  @commands.command()
  async def rdmvid(self, ctx):
    vid_list = [
    "https://cdn.discordapp.com/attachments/824768629631221770/825637401376456744/owo.mp4",
    "https://cdn.discordapp.com/attachments/824768629631221770/825491856548036628/Mec_qui_rage_poir_ses_200k.mp4",
    "https://cdn.discordapp.com/attachments/824768629631221770/825491855301935104/snatched2-1.mp4",
    "https://cdn.discordapp.com/attachments/824768629631221770/825491540457422848/R7aEG3IHnnSP7xoE.mp4",
    "https://cdn.discordapp.com/attachments/824768629631221770/825491135283331123/SPOILER_b1f8f851b092e45fd3c2f43bc93101d5.mp4",
    "https://cdn.discordapp.com/attachments/824769408257622057/825515067621638205/assad_v2.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829238847216287794/1_1.mov",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239553259864084/1_2.mov",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239556297457664/1_3.mov",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239560839102464/1_4.mov",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239921168220160/1_3.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239921600102450/1_1.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239925093433394/1_4.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239924188119081/1_2.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239937432944650/1_9.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239945180741663/1_8.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239944631418900/1_7.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239945234612264/1_6.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239961156321290/1_10.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829239980152586330/1_13.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829241672134033479/1_19.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829242154294706196/1_173.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829242502090326016/1_40.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829242677269889094/1_42.mp4",
    "https://cdn.discordapp.com/attachments/722842924345458709/829243818988797952/1_156.mp4",
    "https://cdn.discordapp.com/attachments/719960352028360796/883250398461317120/video0.mp4",
    "https://cdn.discordapp.com/attachments/824034311371096115/839601189129682955/Mario_kill.mp4",
    "https://cdn.discordapp.com/attachments/824034311371096115/828710092933038080/video0.mov",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635622739337246/1.mp4",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635637297741824/170046522_3627516120806935_3086048620591851321_n.mp4",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635735272509460/239987173_1414993918901364_8346387454969778095_n.mp4",
    "https://cdn.discordapp.com/attachments/719960352028360796/883635779581132810/240144362_546681999921101_4613012557642058491_n.mp4"]
    
    await ctx.send(f"{random.choice(vid_list)}")

  @commands.command()
  async def serverinfo(self, ctx):
    embed = nextcord.Embed(title=f"{ctx.guild.name}", timestamp=datetime.datetime.utcnow(), color=nextcord.Color.blue())
    embed.add_field(name="Serveur créé le", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Propriétaire du serveur", value=f"{ctx.guild.owner}")
    embed.add_field(name="Région du serveur", value=f"{ctx.guild.region}")
    embed.add_field(name="ID du serveur", value=f"{ctx.guild.id}")
    embed.add_field(name = "Roles", value = len(ctx.guild.roles))
    embed.add_field(name = "AFK Timeout", value = "{:g} min.".format(ctx.guild.afk_timeout / 60))
    embed.add_field(name = "AFK Channel", value = str(ctx.guild.afk_channel))
    channel_types = [c.type for c in ctx.guild.channels]
    text_count = channel_types.count(nextcord.ChannelType.text)
    voice_count = channel_types.count(nextcord.ChannelType.voice)
    embed.add_field(name = "Channels", value = "{} text\n{} voice".format(text_count, voice_count))
    embed.add_field(name = "Members", value = "{}\n({} bots)".format(ctx.guild.member_count, sum(m.bot for m in ctx.guild.members)))
    embed.add_field(name = "Verification Level", value = str(ctx.guild.verification_level).capitalize())
    embed.add_field(name = "2FA Requirement", value = bool(ctx.guild.mfa_level))
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://img.icons8.com/ios/50/000000/ingredients-list.png")

    await ctx.send(embed=embed)

  @commands.command()
  async def userinfo(self, ctx,user:nextcord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        return
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = nextcord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar),
    embed.set_footer(text=f'Requested by - {ctx.author}',icon_url=ctx.author.avatar)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)

  
 
    embed.add_field(name='Bot?',value=user.bot,inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed)


  @commands.command()
  async def version(self, ctx):
    embed = nextcord.Embed(title=f"Bot: Hyko", timestamp=datetime.datetime.utcnow(), color=nextcord.Color.blue())
    embed.add_field(name="Bot créé le", value=f"01/09/2021",inline=False)
    embed.add_field(name="Propriétaire / créateur du bot", value=f"**zzAdri#0001**",inline=False)
    embed.add_field(name="ID du bot", value=f"552174858985799680",inline=False)
    embed.add_field(name="Version du bot", value=f"{config.BOT_VERSION}",inline=False)
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://img.icons8.com/ios/50/000000/ingredients-list.png")

    await ctx.send(embed=embed)


  @commands.command()
  async def math(self, ctx, question1:int, symbol:str, question2:int):
    if symbol == "+":
      embed = nextcord.Embed (title=f"la somme de {question1} + {question2}:", description=question1+question2, color=random.choice(config.COLORS))
      embed.set_thumbnail(url="https://img.icons8.com/color/50/000000/calculate.png")
      await ctx.reply(embed=embed)
    elif symbol == "-":
      embed = nextcord.Embed (title=f"la somme de {question1} - {question2}:", description=question1-question2, color=random.choice(config.COLORS))
      embed.set_thumbnail(url="https://img.icons8.com/color/50/000000/calculate.png")
      await ctx.reply(embed=embed)
    elif symbol == "*":
      embed = nextcord.Embed (title=f"la somme de {question1} * {question2}:", description=question1*question2, color=random.choice(config.COLORS))
      embed.set_thumbnail(url="https://img.icons8.com/color/50/000000/calculate.png")
      await ctx.reply(embed=embed)
    elif symbol == "/":
      embed = nextcord.Embed (title=f"la somme de {question1} / {question2}:", description=question1/question2, color=random.choice(config.COLORS))
      embed.set_thumbnail(url="https://img.icons8.com/color/50/000000/calculate.png")
      await ctx.reply(embed=embed)
    else:
      embed=nextcord.Embed(title="**Erreur**", description="je ne suis capable de comprendre que **``+``**,  **``-``**,  **``/``**,  **``*``**. ", color=config.ERROR_COLOR)
      embed.set_author(name="Hyko", url="https://discord.com/invite/BVpNgUxRZ2", icon_url="https://cdn.discordapp.com/avatars/552174858985799680/846123c387918e619c9f8e3d983f1da1.png")
      embed.set_thumbnail(url="https://img.icons8.com/ios/452/database-error.png")
      await ctx.send(embed=embed)




  @commands.command()
  async def counter(self, ctx: commands.Context):
      await ctx.send('Appuis !', view=main.Counter())

  @commands.command()
  async def morpion(self, ctx: commands.Context):
      await ctx.send('Morpion: X commence en premier', view=main.TicTacToe())

  @commands.command()
  async def google(self, ctx: commands.Context, *, query: str):
      embed=nextcord.Embed(title=f"Google Resulta pour: `{query}`", color=random.choice(config.COLORS))
      embed.set_thumbnail(url="https://img.icons8.com/color/50/000000/google-logo.png")
      await ctx.send(embed=embed, view=main.Google(query))


def setup(client):
  client.add_cog(Fun(client))
  print("Fun Cog is load")