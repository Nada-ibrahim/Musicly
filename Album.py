from typing import List
import Song
import Band


class Album:
    band: Band
    #songs: List[Song]

    def __init__(self, title, band):
        self.band = band
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
