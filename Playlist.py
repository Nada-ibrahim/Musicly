from typing import List

import Song

class Playlist:
    songs: List[Song]

    def __init__(self, name, description, tracks_no):
        self.name = name
        self.description = description
        self.tracks_no = tracks_no
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
