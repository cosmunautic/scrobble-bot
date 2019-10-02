Scrobble to Last.fm when listening to music on Discord using Fredboat
--
## You'll want to use this code as a baseline to create your own bot to be used in your own personal servers!

Disclaimer: I made this for personal use, it is a little irritating to use, but after hours of time listening to music with lost scrobbles I created this simple tool. The biggest flaw is in the fact that Fredboat's responses (and those of most bots) are formatted with blank space etc. so that other bots don't respond. Always remember, after song selection, copy Fred's message that confirms your choice, that is how you will scrobble. ^_^


**Create Bot**

1: Go to discordapp.com/developers/applications/me and create a new application, name it something scrobble-icious and save
2: Now, on the right-hand menu, click Bot -> Build-a-bot -> Add bot (your new app with the scrobble-icious name)
3: Add bot to desired server, find client ID under App Details and go to url https://discordapp.com/oauth2/authorize?&client_id=CLIENTID&scope=bot&permissions=8


**Edit source code to get your bot to scrobble to your lastfm!**

You'll need bots authorization token, insert that on line 20 in 'botload.py'
EXAMPLE: TOKEN = "NTk5MDE5NTM4ODE4MDA3MDU1.XSfGyA.ZmD23e7VijZ7n_so0NNVwfhF7NE"

* Add in your own username & password

username = ""
password_hash = pylast.md5("")

EXAMPLE:
username = "scrobble_bot"
password_hash = pylast.md5("mypr0ject!")

* For each additional member of server that wants to scrobble

above @client.event add:
 
username_n = ""
password_hash_n = pylast.md5("")

network_n = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                         username=username_n, password_hash_n=password_hash)
                    
                    
Below @client.event add:
network_n.scrobble(artist="{}".format(songartist), title="{}".format(songtitle),timestamp=int(time.time()))

**Using Bot**

from your commandline, run botload.py 
(If within its directory)
$python botload.py

Your bot will then appear online in your server! 

As you play music using Fredboat **you will need to copy, paste and send the message displayed by Fred** after you choose an option to play. 
For example: 

Fredboat: Song #1 has been selected: The Hotelier - Goodness Pt. 2 (04:00)]
you: Song #1 has been selected: The Hotelier - Goodness Pt. 2 (04:00)]

scrobblebot will respond with song title and artist that it has scrobbled to your account!!


