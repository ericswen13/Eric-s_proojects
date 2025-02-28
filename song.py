class Song:
    def __init__(self, artist_name, album_name, song_name):
        self.artist_name = artist_name
        self.album_name = album_name
        self.song_name = song_name
    
    def __str__(self):
        return f"Artist Name: {self.artist_name}, Album Name: {self.album_name}, Song Name: {self.song_name}"
    
    def get_artist_name(self):
        return self.artist_name
    
    def set_artist_name(self, artist_name):
        self.artist_name = artist_name

    def get_album_name(self):
        return self.album_name
    
    def set_album_name(self, album_name):
        self.album_name = album_name

    def get_song_name(self):
        return self.song_name
    
    def set_song_name(self, song_name):
        self.song_name = song_name

