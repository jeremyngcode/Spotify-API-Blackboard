Spotify API Blackboard
======================

Intro
-----
As a pianist musician with an [online streaming catalog](https://open.spotify.com/artist/6mdGjVrAY95ecXnVgtefti), Spotify was naturally what I explored when I first started learning about APIs.

This project is a 'blackboard' because I use it for general purposes like drafting code or retrieving data as and when. It was initially an automation script which I plan to post soon, but I have since made a separate repo and Spotify client ID for it, as I wanted to have a dedicated place to write random code for interacting with Spotify's web API.

Getting Started
---------------
### 1. Create App
- Login to [Spotify for Developers](https://developer.spotify.com) and click on 'Create app' in your dashboard.
- Fill in required fields:
  1. App name (can be anything)
  2. App description (can be anything)
  3. Redirect URI: http://localhost:8080/callback
- Go to your newly created app settings and note the following:
  1. Client ID
  2. Client Secret

### 2. Configure [settings.py](settings.py)
- Fill in your `CLIENT_ID` and `CLIENT_SECRET`:
  ```
  # Example
  CLIENT_ID = 'abc-my-client-id-123'
  CLIENT_SECRET = 'abc-my-client-secret-123'
  ```
  I have also provided a .env template file to use with `load_dotenv()`.
- Make sure `redirect_uri` is the same as the one you entered in your app.
- Depending on the data you want to retrieve, you may need to fill in `scopes`. This determines what kind of data your app is allowed access to. If you need more than the two I've provided as the default, a list of scopes can be found [here](https://developer.spotify.com/documentation/web-api/concepts/scopes).

### 3. Authorize App
- Run [oauth.py](oauth.py) in your terminal / cmd.
- In the opened web browser, login to your Spotify account if you haven't already.
- Click 'Agree' to grant the relevant access permissions to your app. 
- In the address bar, copy everything after `code=` and paste it in the terminal.
- Hit enter. If all went well, you should see your token details printed.

Go to [Blackboard.py](Blackboard.py) and start writing code!

The access token expires in 60 mins, but you will not have to worry about this as I have coded it in such a way that it will refresh whenever required.

Usage ([functions.py](functions.py))
------------------------------------
Most of the functions will require a [Spotify ID](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) as its first argument.
```
# Example
myself = get_artist('22characters-SpotifyID')
custom_printer.pprint(myself)

my_name = myself['name']
my_followers = myself['followers']['total']
my_pop = myself['popularity']

print(
  f'I am {my_name} and I have {int(my_followers)} followers! '
  f'My popularity index is {my_pop}! Am I famous yet??'
)
```
There are currently about 10 functions for use, but I may include more.

Extra Thoughts
--------------
- One thing I found interesting while working on this and exploring Spotify's API was that there is actually such a thing as a popularity metric. I googled this and apparently it is called the 'popularity index'. Admittedly, I check my popularity index from time to time. 😅
- I know there is already another library ([Spotipy](https://pypi.org/project/spotipy)) that does what I'm doing here, but I figured I would learn a lot more if I coded this from scratch with just the requests library. I've also gained a better understanding of the oauth process through writing this. Plus, it was fun anyway. 😁

#### Notable libraries used / learned for this project:
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
