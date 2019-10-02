Scrobble to Last.fm when listening to music on Discord using Fredboat
--

## You'll want to use this code as a baseline to create your own bot to be used in your own personal servers!


**Create Bot**

1: Go to discordapp.com/developers/applications/me and create a new application, name it something scrobble-icious and save

2: Now, on the right-hand menu, click Bot -> Build-a-bot -> Add bot (your new app with the scrobble-icious name)

3: Add bot to desired server, find client ID under App Details and go to url https://discordapp.com/oauth2/authorize?&client_id=CLIENTID&scope=bot&permissions=8


**Edit source code to get your bot to scrobble to your lastfm!**

1. You'll need bots authorization token, which you will find under the information about this app bot user, once you *click to reveal token*

Insert token on line 20 in 'botload.py'
 EXAMPLE: 

``` python
TOKEN = "NTk5MDE5NTM4ODE4MDA3MDU1.XSfGyA.ZmD23e7VijZ7n_so0NNVwfhF7NE"
```

2. Add in your own username & password

```python
username = "username"
password_hash = pylast.md5("password")
```

EXAMPLE:
```python
> username = "scrobble_bot"
> password_hash = pylast.md5("mypr0ject!")
```
##### *note: by default, all scrobbles that result from use of this code will track to last.fm user scrobble_bot, you can easily remove this, but I think it'll be fun to have <3*

3. For each additional member of server that wants to scrobble

*above '@client.event' in code (line 33 in original)* add:
 
```python
username_n = "username_n"
password_hash_n = pylast.md5("password_n")

network_n = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                         username=username_n, password_hash_n=password_hash)
```                    
                    
*below @client.event* add:
```python 
network_n.scrobble(artist="{}".format(songartist), title="{}".format(songtitle),timestamp=int(time.time()))
```
**Using Bot**

from your commandline, run botload.py 
(If within directory containing code)

> $python botload.py

Your bot will then appear online in your server! 

##### *Disclaimer: I made this for personal use, after hours of time listening to music with lost scrobbles I created this simple tool to keep track of music I listened to with my pals. It is a little irritating to use..The biggest flaw is in the fact that Fredboat's responses (and those of most bots) are formatted with blank space etc. so that other bots don't respond.

##### To get around this, after song selection: copy and re-send Fred's message that confirms your choice, that is how you will scrobble. ^_^ 

As you play music using Fredboat **you will need to copy, paste and send the message displayed by Fred** after you choose an option to play. 
For example: 

> Fredboat: Song #1 has been selected: The Hotelier - Goodness Pt. 2 (04:00)]

> you: Song #1 has been selected: The Hotelier - Goodness Pt. 2 (04:00)]

scrobblebot will respond with song title and artist that it has scrobbled to your account!!


