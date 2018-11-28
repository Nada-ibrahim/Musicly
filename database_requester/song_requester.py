import Song
from sqliteDB.musicly_db import MusiclyDB


class SongRequester:
    db: MusiclyDB

    def __init__(self, db):
        self.db = db

    def get_song_information(self, song_name):
        print(self.db.get_song_info(song_name))

    def get_band_songs(self, band_name):
        print()
        # TODO: get all songs name, duration and URL sang by a certain band from database

    def get_artist_songs(self, artist_name):
        print()
        # TODO: get all songs name, duration and URL sang by a certain artist whether in band or solo from database

    def get_genre_songs(self, genre_name):
        print()
        # TODO: get all songs name, duration and URL in a certain genre from database

    def remove_song(self, song_name):
        self.db.remove_song(song_name)
        # TODO: remove a song from database