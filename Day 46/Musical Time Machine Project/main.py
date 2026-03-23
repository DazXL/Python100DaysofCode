import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_id = os.getenv("SPOTIFY_ID")
spotify_key = os.getenv("SPOTIFY_SECRET")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_id,
                                               client_secret=spotify_key,
                                               redirect_uri="https://example.com/",
                                               scope="playlist-modify-private", cache_path="token.txt"))

'''results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])'''

'''results = sp.current_user()
print(results)'''


date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD:")



header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}

url = "https://www.officialcharts.com/charts/singles-chart/"
response = requests.get(url+date, headers = header)

soup = BeautifulSoup(response.text, 'html.parser')
song_titles = [song.text for song in soup.select('div.description.block > p > a.chart-name.font-bold.inline-block > span:nth-child(2)')]
artists = [artist.text for artist in soup.select('div.chart-item-content.relative.flex.w-full > div.description.block > p > a.chart-artist.text-lg.inline-block > span')]
final_list = []

for x in range(len(song_titles)):
    song = f"{song_titles[x].title()} by {artists[x].title()}"
    final_list.append(song)

year = date.split("-")[0]
print(year)
song_uris = []
user_id = sp.current_user()['id']

for song in final_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)