from django.shortcuts import render

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



client_credentials_manager = SpotifyClientCredentials(
        client_id='---------------------------------------',
        client_secret='-------------------------------------')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('roykebab')

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print ("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None


# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")


