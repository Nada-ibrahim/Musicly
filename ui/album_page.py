
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

            album_title_id_songs = self._db.get_all_albums()
            headers = ["Title", "ID" "Songs No."]
            self.print_list(headers, album_title_id_songs)

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
        headers = ["Band Name"]
        artists_list, bands_list = self._db.get_all_Artists()
        self.print_attrs(headers, bands_list)
        band_name = input("Enter name of the band/artist: ")
        songs = self._db.get_all_songs()
        headers = ["Song Name", "Song Length", "Song URL", "Release Date", "Band"]
        self.print_attrs(headers, songs)
        print("Enter all URLs of bands songs: ")
        songs_url = input().split(' ')
        # TODO: add songs urls to album
        self._db.add_album(band_name, title)

    def remove_album(self):
        id = input("Enter album ID: ")
        self._db.delete_album(id)

    def view_album(self):
        id = input("Enter ID: ")
        album = self._db.get_album_information(id)
        p = SongsPage(self._db, album.songs, album.band)