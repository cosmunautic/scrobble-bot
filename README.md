# scrobble-bot
a scrobble bot for use with fredboat on discord,  right now this is specified to fredboat based on formatting of messages! 

1. Add in your own username & password

username = ""
password_hash = pylast.md5("")

2. For each additional member of server that wants to scrobble, above @client.event add:
 
username_n = ""
password_hash_n = pylast.md5("")

network_n = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                         username=username_n, password_hash_n=password_hash)
                    
                    
Below @client.event add:

network_n.scrobble(artist="{}".format(songartist), title="{}".format(songtitle),timestamp=int(time.time()))
