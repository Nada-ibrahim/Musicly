from sqlite3 import Date

from ui.page import Page
from ui.songs_page import SongsPage


class AlbumPage(Page):
    def __init__(self, db):
        super().__init__(db)
        while True:
            self.print_title("All songs")

            songs = self._db.get_all_songs()
            headers = ["Song Name", "Song Length", "Song URL", "Release Date", "Band"]
            self.print_attrs(headers, songs)

            print("\n1- Add Song")
            print("2- Remove Song")
            print("3- View all songs in Genre")
            print("4- Back")

            while True:
                n = int(input("\nEnter Your Choice: "))
                if n == 1:
                    self.add_song()
                    break
                elif n == 2:
                    self.remove_song()
                    break
                elif n == 3:
                    self.view_all_songs_in_genre()
                    break
                elif n == 4:
                    return
                else:
                    print("INVALID NUMBER")

    def add_song(self):
        name = input("Enter name: ")
        url = input("Enter URL: ")

        headers = ["Band Name"]
        artists_list, bands_list = self._db.get_all_Artists()
        self.print_attrs(headers, bands_list)
        band_name = input("Enter name of the band/artist: ")

        album_title_id_songs = self._db.get_all_albums()
        headers = ["Title", "ID", "Songs No."]
        self.print_list(headers, album_title_id_songs)
        album_id = input("Enter Album ID: ")

        day = int(input("Enter day of release: "))
        month = int(input("Enter month of release: "))
        year = int(input("Enter year of release: "))
        release_date = Date(year, month, day)

        duration = input("Enter Song Duration: ")
        lyrics = input("Enter Song lyrics: ")

        print("Enter all Genres of the song: ")
        songs_genres = input().split(' ')

        # TODO: add list of genres to addSong
        self._db.add_song(songs_genres, url, album_id, band_name
                          , name, release_date, lyrics, duration)

    def remove_song(self):
        name = input("Enter Song Name: ")
        self._db.remove_song(name)

    def view_all_songs_in_genre(self):
        genre = input("Enter genre: ")
        songs = self._db.get_genre_songs(genre)
        p = SongsPage(self._db, songs, genre)
