--
title: Scrobble to Last.fm when listening to music on Discord using Fredboat
--
## You'll want to use this code as a baseline to create your own bot to be used in your own personal servers!

**Create Bot**

1: Go to discordapp.com/developers/applications/me and create a new application, name it something scrobble-icious and save
2: Now, on the right-hand menu, click Bot -> Build-a-bot -> Add bot (your new app with the scrobble-icious name)
3: Add bot to desired server, find client ID under App Details and go to url https://discordapp.com/oauth2/authorize?&client_id=CLIENTID&scope=bot&permissions=8


**Edit source code to get your bot to scrobble to your lastfm!**

You'll need bots authorization token, insert that on line 20 in 'botload.py'
EXAMPLE: TOKEN = "NTk5MDE5NTM4ODE4MDA3MDU1.XSfGyA.ZmD23e7VijZ7n_so0NNVwfhF7NE"

1. Add in your own username & password

username = ""
password_hash = pylast.md5("")

EXAMPLE:
username = "scrobble_bot"
password_hash = pylast.md5("mypr0ject!")

2. For each additional member of server that wants to scrobble, above @client.event add:
 
username_n = ""
password_hash_n = pylast.md5("")

network_n = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                         username=username_n, password_hash_n=password_hash)
                    
                    
Below @client.event add:
network_n.scrobble(artist="{}".format(songartist), title="{}".format(songtitle),timestamp=int(time.time()))

**Run Bot**
$python botload.py

Your bot will appear in your server

As you play music using Fredboat copy, paste and send the message displayed after you make your choice on which displayed option to play. 
For example: "Song #1 has been selected: The Hotelier - Goodness Pt. 2 (04:00)]"

scrobblebot will respond with song - artist scrobbled
"Goodness Pt. 2  -  The Hotelier"
