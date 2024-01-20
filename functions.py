import requests
from requests.exceptions import Timeout
from oauth import retrieve_token_info
# -------------------------------------------------------------------------------------------------

# Spotify Web API
BASE_API_URL = "https://api.spotify.com/v1"

def _get(url, **kwargs):
	access_token = retrieve_token_info()['access_token']
	headers = {'Authorization': f'Bearer {access_token}'}

	try:
		response = requests.get(url, headers=headers, params=kwargs, timeout=5)
	except Timeout:
		print('[UNSUCCESSFUL RETRIEVAL - Timed out..]')
	else:		
		if response.status_code == 200:
			data = response.json()
			print('[200 OK - SUCCESSFUL RETRIEVAL]')
			print('-' * 100)
			return data
		else:
			print(f'[{response.status_code} {response.reason}]')
	print('-' * 100)

def get_artist(artist_id):
	url = BASE_API_URL + f"/artists/{artist_id}"

	print(f'get_artist({artist_id}):')
	return _get(url)

def get_artists_albums(artist_id, include_groups=None, market=None, limit=50, offset=0):
	url = BASE_API_URL + f"/artists/{artist_id}/albums"
	params = {
		'include_groups': include_groups,
		'market': market,
		'limit': limit,
		'offset': offset
	}

	print(f'get_artists_albums({artist_id}):')
	return _get(url, **params)

def get_album(album_id, market=None):
	url = BASE_API_URL + f"/albums/{album_id}"
	params = {
		'market': market
	}

	print(f'get_album({album_id}):')
	return _get(url, **params)

def get_track(track_id, market=None):
	url = BASE_API_URL + f"/tracks/{track_id}"
	params = {
		'market': market
	}

	print(f'get_track({track_id}):')
	return _get(url, **params)

def get_playlist(playlist_id, fields=None, market=None):
	url = BASE_API_URL + f"/playlists/{playlist_id}"
	params = {
		'fields': fields,
		'market': market
	}

	print(f'get_playlist({playlist_id}):')
	return _get(url, **params)

def get_current_users_profile():
	url = BASE_API_URL + "/me"

	print('get_current_users_profile():')
	return _get(url)

def get_current_users_saved_albums(market=None, limit=50, offset=0):
	url = BASE_API_URL + "/me/albums"
	params = {
		'market': market,
		'limit': limit,
		'offset': offset
	}

	print('get_current_users_saved_albums():')
	return _get(url, **params)

def get_current_users_playlists(limit=12, offset=0):
	url = BASE_API_URL + "/me/playlists"
	params = {
		'limit': limit,
		'offset': offset
	}

	print('get_current_users_playlists():')
	return _get(url, **params)
