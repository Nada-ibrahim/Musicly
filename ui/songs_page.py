
from ui.page import Page

class SongsPage(Page):
    def __init__(self, db, songs, text = None):
        super().__init__(db)
        while True:
            self.print_title("Songs")
            if not text == None:
                print(text)
            headers = ["Song Name", "Duration", "Song URL"]
            self.print_attrs(headers, songs)

            print("1- Play Song")
            print("2- Play all songs")
            print("3- Back")

            while True:
                n = int(input("Enter Your Choice: "))
                if n == 1:
                    # TODO: Play song
                    break
                elif n == 2:
                    # TODO: Play all songs
                    break
                elif n == 3:
                    return
                else:
                    print("INVALID NUMBER")