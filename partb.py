import requests
from album import Album
from song import Song

url = 'https://itunes.apple.com/us/rss/topsongs/limit=100/json'
response = requests.get(url)
data = response.json()

topsongs = []
album_dict = {}

for entry in data['feed']['entry']:
    artist_name = entry['im:artist']['label']
    album_name = entry['im:collection']['im:name']['label']
    song_name = entry['title']['label']
    
    song = Song(artist_name, album_name, song_name)
    
    if album_name in album_dict:
        album_dict[album_name].add_song(song)
    else:
        album = Album(album_name)
        album.add_song(song)
        album_dict[album_name] = album
    
    topsongs.append(song)

def search_artist_with_albums(topsongs, artist_name):
    found = False
    for album in album_dict.values():
        if album.song_list[0].get_artist_name().lower() == artist_name.lower():
            print(f"Artist Name: {artist_name}")
            print(album)
            found = True
    if not found:
        print("No artist found")
        
artist_name_input = input("Enter the artist name: ")
search_artist_with_albums(topsongs, artist_name_input)
