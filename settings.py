from os import environ
from dotenv import load_dotenv
import pprint
# -------------------------------------------------------------------------------------------------

load_dotenv()

# EDIT ACCORDINGLY
CLIENT_ID = environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = environ.get('SPOTIFY_CLIENT_SECRET')
redirect_uri = "http://localhost:8080/callback"

scopes = (
	'user-library-read',
	'playlist-read-private'
)

custom_printer = pprint.PrettyPrinter(
	depth=None,
	indent=1,
	width=100,
	sort_dicts=False,
	compact=False
)
