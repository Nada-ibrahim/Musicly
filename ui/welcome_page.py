from ui.album_page import AlbumPage
from ui.artist_page import ArtistPage
from ui.playlist_page import PlaylistPage
from ui.page import Page

class WelcomePage(Page):
    def __init__(self, db):
        super().__init__(db)

        while True:
            self.print_title("Welcome to Musicly")
            print("1- Playlists")
            print("2- Artists")
            print("3- Albums")
            print("4- library")
            while True:
                n = int(input("\nEnter Your Choice: "))
                if n == 1:
                    PlaylistPage(self._db)
                    break
                elif n == 2:
                    ArtistPage(self._db)
                    break
                elif n == 3:
                    AlbumPage(self._db)
                    break
                elif n == 4:
                    break
                else:
                    print("INVALID NUMBER")

