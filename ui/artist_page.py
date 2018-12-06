from sqlite3 import Date

from Artist import Artist
from ui.band_page import BandPage
from ui.page import Page
from ui.songs_page import SongsPage


class ArtistPage(Page):
    def __init__(self, db):
        super().__init__(db)
        while True:
            self.print_title("Artists")

            artists_list, bands_list = self._db.get_all_Artists()
            headers = ["Name"]
            self.print_attrs(headers, artists_list)

            print("\n1- Add Artist")
            print("2- Remove Artist")
            print("3- View All Songs by Artist")
            print("4- Switch to Band")
            print("5- Back")

            while True:
                n = int(input("\nEnter Your Choice: "))
                if n == 1:
                    self.add_artist()
                    break
                elif n == 2:
                    self.remove_artist()
                    break
                elif n == 3:
                    self.view_all_songs_by_artist()
                    break
                elif n == 4:
                    BandPage(self._db)
                    break
                elif n == 5:
                    return
                else:
                    print("INVALID NUMBER")

    def add_artist(self):
        name = input("Enter name: ")
        day = int(input("Enter day of birth: "))
        month = int(input("Enter month of birth: "))
        year = int(input("Enter year of birth: "))
        date = Date(year, month, day)
        artist = Artist(name, date)
        self._db.add_artist(artist)

    def remove_artist(self):
        name = input("Enter Name: ")
        self._db.remove_artist(name)

    def view_all_songs_by_artist(self):
        name = input("Enter Name: ")
        songs = self._db.get_artist_songs(name)
        p = SongsPage(self._db, songs)