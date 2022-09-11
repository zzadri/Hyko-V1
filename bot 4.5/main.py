## import

from nextcord.flags import Intents
from typing import List
from functools import update_wrapper
from urllib.parse import quote_plus
from itertools import cycle
import nextcord
import json
import traceback
import sys
import platform
import os
import random
import youtube_dl
import asyncio
import nextcord.utils
from nextcord import Embed
from nextcord import client
from nextcord.ext import commands, tasks
from nextcord.ext.commands.core import command





## liaison avec le dossier config

if not os.path.isfile("config.py"):
	sys.exit("'config.py' est introuvable !")
else:
	import config


# prefix

def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]


default_intents = nextcord.Intents.default()
default_intents.members = True
default_intents.bans = True
default_intents.messages = True

client = commands.AutoShardedBot(command_prefix= get_prefix, intents=default_intents, help_command=None)

#shard_count=10,

pfp_path = "pp.png"
fp = open(pfp_path, 'rb')
pfp = fp.read()

# load

@client.event
async def on_ready():
  print("-------------------")
  print(f"Logged in as {client.user.name}")
  print(f'ID : {client.user.id}')
  print(f"nextcord.py API version: {nextcord.__version__}")
  print(f"Python version: {platform.python_version()}")
  print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
  print("-------------------")
  await client.change_presence(activity=nextcord.Streaming(name="discord.gg/procommu", url="https://www.twitch.tv/zzAdri"))
  await client.user.edit(avatar=pfp)
  uptimeCounter.start()
  
	# status_swap.start()






ts = 0
tm = 0
th = 0
td = 0

@tasks.loop(seconds=2.0)
async def uptimeCounter():
  global ts, tm, th, td
  ts += 2
  if ts == 60:
    ts = 0
    tm = +1
    if tm == 60:
      tm = 0
      th += 1
      if th == 24:
        th = 0
        td =+ 1

@uptimeCounter.before_loop
async def beforeUptimeCounter():
  await client.wait_until_ready()


# prefix perso
@client.event
async def on_guild_join(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)] = '*'

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes.pop(str(guild.id))

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)



#lvlsys
@client.event
async def on_member_join(member):
  with open('users.json', 'r') as f:
    users = json.load(f)

  await update_data(users, member)

  with open('users.json', 'w') as f:
    json.dump(users, f, indent=4)
  

@client.event
async def on_message(message):
  if message.author.bot == False:
    with open('users.json', 'r') as f:
      users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message)

    with open('users.json', 'w') as f:
      json.dump(users, f, indent=4)
  
  await client.process_commands(message)



@client.command()

async def update_data(users, user):
  if not f'{user.id}' in users:
    users[f'{user.id}'] = {}
    users[f'{user.id}']['experience'] = 0
    users[f'{user.id}']['level'] = 1  

async def add_experience(users, user, exp):
  users[f'{user.id}']['experience'] += exp

async def level_up(users, user, message):
  with open('levels.json', 'r',) as g:
    levels = json.load(g)
  experience = users[f'{user.id}']['experience']
  lvl_start = users[f'{user.id}']['level']
  lvl_end = int(experience ** (1/4))
  if lvl_start < lvl_end:
    await message.channel.send(f'{user.mention} à lvlup ! il est lvl {lvl_end}')
    users[f'{user.id}']['level'] = lvl_end

@client.command()
async def level(ctx, member: nextcord.Member = None):
  if not member:
    id = ctx.message.author.id
    with open('users.json', 'r') as f:
      users = json.load(f)
    lvl = users[str(id)]['level']
    await ctx.send(f'tu est au level **{lvl}** !')
  else:
    id = member.id
    with open('users.json', 'r') as f:
      users = json.load(f)
    lvl = users[str(id)]['level']
    await ctx.send(f'{member.mention} est au level **{lvl}** !')



















@client.command()
async def load(ctx, extention):
  client.load_extension(f'cogs.{extention}')

@client.command()
async def unload(ctx, extention):
  client.unload_extension(f'cogs.{extention}')
















for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')




















class TicTacToeButton(nextcord.ui.Button['TicTacToe']):
    def __init__(self, x: int, y: int):

        super().__init__(style=nextcord.ButtonStyle.secondary, label='\u200b', row=y)
        self.x = x
        self.y = y

    async def callback(self, interaction: nextcord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = nextcord.ButtonStyle.danger
            self.label = 'X'
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "C'est maintenant au tour de O"
        else:
            self.style = nextcord.ButtonStyle.success
            self.label = 'O'
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "C'est maintenant au tour de X"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = 'X a gagné !'
            elif winner == view.O:
                content = 'O a gagné !'
            else:
                content = "match-nul !"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)


class TicTacToe(nextcord.ui.View):
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None














class Counter(nextcord.ui.View):

    @nextcord.ui.button(label='0', style=nextcord.ButtonStyle.red)
    async def count(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        number = int(button.label) if button.label else 0
        if number + 1 >= 90000000000000000000000000:
            button.style = nextcord.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        await interaction.response.edit_message(view=self)















class Google(nextcord.ui.View):
  def __init__(self, query: str):
    super().__init__()
    query = quote_plus(query)
    url = f'https://www.google.com/search?q={query}'

    self.add_item(nextcord.ui.Button(label='Click ici', url=url))























## sys music

musics = {}
ytdl = youtube_dl.YoutubeDL()


class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

@client.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []

@client.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@client.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()


@client.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    source = nextcord.PCMVolumeTransformer(nextcord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), client.loop)

    client.play(source, after=next)


@client.command()
async def play(ctx, url):
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()

        playembed= nextcord.Embed(title="**Musique**", color=random.choice(config.COLORS))
        playembed.add_field(name=f"Je lance :", value=f"{video.url}")
        playembed.set_thumbnail(url="https://img.icons8.com/nolan/50/musically.png")

        await ctx.send(embed = playembed)
        play_song(client, musics[ctx.guild], video)









client.run(config.TOKEN)