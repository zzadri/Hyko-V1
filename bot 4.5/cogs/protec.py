from typing import Counter
import nextcord
import os
import sys
import json
from nextcord import client
import config
import asyncio
import random
import inspect
import datetime
import nextcord.utils
from nextcord.ext import commands
from nextcord import Embed






# liasion avec autre fichier

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)



class Protec(commands.Cog, name='protec'):

  def __init__(self,client):
    self.client = client


  @commands.Cog.listener()
  async def on_ready(self):
    while True:
      await asyncio.sleep(5)
      with open("spam.txt", "r+") as file:
        file.truncate(0)



  @commands.Cog.listener()
  async def on_message(self, message):

    counter = 0

    with open("spam.txt", "r+") as file:
      for lines in file:
        if lines.strip("\n") == str(message.author.id):
          counter +=1
      
      file.writelines(f"{str(message.author.id)}\n")
      if counter > 5:
        await message.guild.ban(message.author, reason = 'spam')
        await asyncio.sleep(1)
        await message.guild.unban(message.author)



    for file in message.attachments:
      if file.filename.endswith((".exe", ".dll", ".ps1", ".bat", ".com", ".apk", ".app", ".bin", ".cmd", ".msi", ".osx", ".out", ".bin", ".run", ".scr", ".command", ".cpl", ".py")):
        await message.delete()


    if message.content.startswith(("https://urlr.me/", "https://bit.ly/", "https://lc.cx/", "https://rb.gy/", "https://tinyurl.com/", "https://ow.ly/", "https://1zbp.short.gy/", "http://fumacrom.com/", "https://cutt.ly/", "https://www.youporn.com", "https://fr.pornhub.com", "https://twitter.com/SmurrLewd", "https://twitter.com/David83782339", "https://twitter.com/SaymanArt", "https://www.reddit.com/r/hentai", "@everyone", "@here")):
      await message.delete()




  






def setup(client):
  client.add_cog(Protec(client))
  print("protec Cog is load")