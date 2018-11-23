from typing import List
import Song
import Band


class Album:
    band: Band
    songs: List[Song]

    def __init__(self, title, band, songs_number):
        self.band = band
        self.title = title
        self.songs_number = songs_number
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
