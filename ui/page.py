import shutil

from sqliteDB.musicly_db import MusiclyDB


class Page:
    _db: MusiclyDB

    def __init__(self, db):
        self.columns = shutil.get_terminal_size().columns
        self._db = db

    def print_title(self, title):
        print()
        print("--------------------------------------------------".center(self.columns))
        print(title.center(self.columns))
        print("--------------------------------------------------".center(self.columns))
        print()

    def print_in_center(self, text):
        print(text.center(self.columns))

    def print_list(self, headers, ls):
        format_str = '{:>24}' * len(headers)
        print(format_str.format(*headers).center(self.columns))
        for i in range(len(ls)):
            print(format_str.format(*ls[i]).center(self.columns))

    def print_attrs(self, headers, ls_objects):
        format_str = '{:>24}' * len(headers)
        print(format_str.format(*headers).center(self.columns))
        for i in range(len(ls_objects)):
            print(format_str.format(*[str(j) for j in ls_objects[i].__dict__.values()]).center(self.columns))

    def print_song_info(self, song):
        print("Song: " + song.name)
        print("Band/Artist: " + str(song.band))
        print("Featured artist/band: " + str(song.featured_artist))
        print("Album: " + song.album)
        print("Release Date: " + song.release_date)
        genres = [i[0] for i in song.genres]
        print("Genres: " + ",".join(genres))