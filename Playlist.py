from typing import List

import Song

class Playlist:

    def __init__(self, name, description, tracks_no = 0):
        self.name = name
        self.description = description
        self.tracks_no = tracks_no
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
