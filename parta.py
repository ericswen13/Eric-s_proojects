import requests
from song import Song


url = 'https://itunes.apple.com/us/rss/topsongs/limit=100/json'
response = requests.get(url)
data = response.json()

topsongs = []
for entry in data['feed']['entry']:
    artist_name = entry['im:artist']['label']
    album_name = entry['im:collection']['im:name']['label']
    song_name = entry['title']['label']
    
    song = Song(artist_name, album_name, song_name)
    topsongs.append(song)

def get_artist_name(song):
    return song.get_artist_name()

def sort_songs_by_artist(songs_list):
    return sorted(songs_list, key=get_artist_name)

topsongs = sort_songs_by_artist(topsongs)

def search_artist(topsongs, artist_name):
    results = [str(song) for song in topsongs if song.get_artist_name().lower() == artist_name.lower()]
    if results:
        for result in results:
            print(result)
    else:
        print("No artist found")

        
artist_name_input = input("Enter the artist name: ")
search_artist(topsongs, artist_name_input)
