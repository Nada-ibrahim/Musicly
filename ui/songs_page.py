from play_song.play import Player
from ui.page import Page
from play_song import play
class SongsPage(Page):
    def __init__(self, db, songs, text = None):
        super().__init__(db)
        self.player = Player()
        while True:
            self.print_title("Songs")
            if not text == None:
                print(text)
            headers = ["Song Name", "Duration"]
            self.print_attrs(headers, songs)

            print("1- Play Song")
            print("2- Play all songs")
            print("3- Back")

            while True:
                n = int(input("Enter Your Choice: "))
                if n == 1:
                    name = input("Enter name: ")
                    self.play_song(name)
                    break
                elif n == 2:
                    # TODO: Play all songs
                    self.play_playlist(songs)
                    break
                elif n == 3:
                    return
                else:
                    print("INVALID NUMBER")

    def play_song(self, song_name):
        url = self._db.get_url_song_by_name(song_name)
        song = self._db.get_song_by_url(url)
        self.print_song_info(song)
        play.play(url)
        print("\n1- Back")
        while True:
            n = int(input("Enter Your Choice: "))
            if n == 1:
                play.close()
                return
            else:
                print("INVALID NUMBER")

    def play_playlist(self, songs):
        self.player.play_multiple_songs(songs)