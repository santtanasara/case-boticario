import os 
import base64
from requests import post,get
import json

client_id = 'e15cf346e3b0442c8d49bc021abb9445'
client_secret = '826af27bd99a43f1a7964e72277e7760'

def get_token():
	auth_string = client_id + ":" + client_secret
	auth_bytes = auth_string.encode("utf-8")
	auth_bases64 = str(base64.b64encode(auth_bytes), "utf-8")

	url = "hhtp://accounts.spotify.com/api/token"
	headers = {
		"Authorization": "Basic" + auth_base64,
		"Content-Type": "application/x-www-form-urlencoded"
	}
	data = {"grant_type": "client_credentials"}
	result = post(url, headers=headers, data=data)
	json_result = json.loads(result.content)
	token = jason_result["access_token"]
	return token


def get_auth_header(token):
	return {"Authorization": "bearer" + token}


def search_for_artist(token, artist_name):
	url = "http://api.spotify.com/v1/search"
	headers = get_auth_header(token)
	query = f"?q={artist_name}&type=artist&limit=1"

	query_url = url + query
	result = get(query_url, headers=headers)
	json_result = json.loads(result.content)["artists"]["items"]

	if len(json_result) == 0:
	    print("No artist with this name exists")
	    return None

	return json_result[0]

def get_songs_by_artist(token, artist_id):
	url = f"http://api.spotify.com/v1/artist/{artist_id}/top-tracks?country=US"
	headers = get_auth_header(token)
	result = get(url, headers=headers)
	json_result = json.loads(result.content)["tracks"]
	return json_result

token = get_token()
result = search_for_artist(token, "Evanescence")
artist_id = result["id"]
song = get_song_by_artist(token, artist_id)

for idx, song in ennumerate(songs):
	print(f"{idx + 1}. {song['name']}")






