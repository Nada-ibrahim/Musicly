
from ui.page import Page
from ui.songs_page import SongsPage


class BandPage(Page):
    def __init__(self, db):
        super().__init__(db)
        while True:
            self.print_title("Bands")

            artists_list, bands_list = self._db.get_all_Artists()
            headers = ["Name"]
            self.print_list(headers, bands_list)

            print("\n1- Add Band")
            print("2- Remove Band")
            print("3- View All Songs by Band")
            print("4- Back")

            while True:
                n = int(input("\nEnter Your Choice: "))
                if n == 1:
                    self.add_band(artists_list)
                    break
                elif n == 2:
                    self.remove_band()
                    break
                elif n == 3:
                    self.view_all_songs_by_band()
                    break
                elif n == 4:
                    return
                else:
                    print("INVALID NUMBER")

    def add_band(self, artist_list):
        name = input("Enter name: ")
        headers = ["Artist Name"]
        self.print_attrs(headers, artist_list)
        print("Enter names of artists in the band: ")
        artists = input().split(' ')
        # TODO add artists to add_band function
        self._db.add_band(name, artists)

    def remove_band(self):
        name = input("Enter Name: ")
        # TODO: add remove band and if band contains one artist remove artist)

    def view_all_songs_by_band(self):
        name = input("Enter Name: ")
        songs = self._db.get_band_songs(name)
        p = SongsPage(self._db, songs)