import nextcord
import os
import sys
import json
from nextcord import client
import nextcord.utils
from nextcord import Embed
import config
import asyncio
import random
import inspect
from nextcord.ext import commands
import datetime

# liasion avec autre fichier

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)



class Fun(commands.Cog, name='Fun'):

  def __init__(self,client):
    self.client = client




def setup(client):
  client.add_cog(Fun(client))
  print("Fun Cog is load")