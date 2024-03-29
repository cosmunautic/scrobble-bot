import discord
import pylast
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
import pylast
import time
from xml.etree import ElementTree
import requests
import time

API_KEY = "a6fe39fa098111e980941a8e9a7cf598"
API_SECRET = "189741a760592902ea7de9c39a53ab68"
BOT_PREFIX = ("**", "Song #")

#insert your own bot token here
TOKEN = ""
client = Bot(command_prefix=BOT_PREFIX)

#insert your own password here
username = ""
password_hash = pylast.md5("")

username_w = "scrobble_bot"
password_hash_w = pylast.md5("mypr0ject!")


network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                         username=username, password_hash=password_hash)

network_w = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                         username=username_w, password_hash=password_hash_w)

@client.event
async def on_message(message):

    if message.content.startswith('Song'): 
        _, songname = message.content.split(':',1)
        songname = songname.split('(',1)
        songname = songname[0]
        songartist = songname.split('-',1)[0]
        songtitle = songname.split('-',1)[1]

        #fullname = '{} is title'.format(songtitle)
        track = network.get_track("{}".format(songtitle),"{}".format(songartist))
        album = network.get_album("{}".format(songartist),"{}".format(songtitle))
        await client.send_message(message.channel, track)
        network.scrobble(artist="{}".format(songartist), title="{}".format(songtitle),timestamp=int(time.time()))

        network_w.scrobble(artist="{}".format(songartist), title="{}".format(songtitle),timestamp=int(time.time()))
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)




