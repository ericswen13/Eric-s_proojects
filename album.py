class Album:
    def __init__(self, album_name):
        self.album_name = album_name
        self.song_list = []
    
    def add_song(self, song):
        self.song_list.append(song)
    
    def __str__(self):
        songs = ', '.join([song.get_song_name() for song in self.song_list])
        return f"Album Name: {self.album_name}, Song Name: {songs}"
    
    def get_album_name(self):
        return self.album_name
    
    def set_album_name(self, album_name):
        self.album_name = album_name
    
    def get_song_list(self):
        return self.song_list
