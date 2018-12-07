
from sqlite3 import Date

from Artist import Artist
from ui.band_page import BandPage
from ui.page import Page
from ui.songs_page import SongsPage


class AlbumPage(Page):
    def __init__(self, db):
        super().__init__(db)
        while True:
            self.print_title("Albums")

            album_id_title_songs = self._db.get_all_albums()
            headers = ["ID", "Title",  "Songs No."]
            self.print_list(headers, album_id_title_songs)

            print("\n1- View Album")
            print("2- Add Album")
            print("3- Remove Album")
            print("4- Back")

            while True:
                n = int(input("\nEnter Your Choice: "))
                if n == 1:
                    self.view_album()
                    break
                elif n == 2:
                    self.add_album()
                    break
                elif n == 3:
                    self.remove_album()
                    break
                elif n == 4:
                    return
                else:
                    print("INVALID NUMBER")

    def add_album(self):
        title = input("Enter Title: ")
        headers = ["Band/Artist Name"]
        bands_list = self._db.get_all_bands()
        artists_list = self._db.get_all_artists()
        self.print_list(headers, bands_list)
        self.print_attrs(["----------"], artists_list)
        band_name = input("Enter name of the band/artist: ")

        # TODO: add songs urls to album
        self._db.add_album(band_name, title)

    def remove_album(self):
        id = input("Enter album ID: ")
        self._db.delete_album(id)

    def view_album(self):
        id = input("Enter ID: ")
        album = self._db.get_album_information(id)
        p = SongsPage(self._db, album.songs, album.band)