from ui.page import Page
from play_song import play


class PlaylistPage(Page):

    def __init__(self, db):
        super().__init__(db)
        while True:
            self.print_title("Playlists")

            playlist_name_id_songs = self._db.get_all_playlists()
            headers = ["ID", "Name", "Tracks No"]
            self.print_list(headers, playlist_name_id_songs)

            print("\n1- View Playlist")
            print("2- Add Playlist")
            print("3- Delete Playlist")
            print("4- Back")
            while True:
                n = int(input("\nEnter Your Choice: "))
                if n == 1:
                    id = input("Enter ID: ")
                    self.view_playlist(id, order_by="playlistID")
                    break
                elif n == 2:
                    self.add_playlist()
                    break
                elif n == 3:
                    id = int(input("Enter id: "))
                    self._db.delete_playlist(id)
                    break
                elif n == 4:
                    return
                else:
                    print("INVALID NUMBER")

    def view_playlist(self, id, order_by):
        while True:
            playlist = self._db.get_playlist_information(id, order_by, "ASC")
            self.print_title(playlist.name)
            print(playlist.description)
            print()
            headers = ["Song Name", "Duration", "Song URL"]
            self.print_attrs(headers, playlist.songs)

            print("1- Play Song")
            print("2- Stop Song")
            print("3- Play Playlist")
            print("4- Sort by")
            print("5- Add Song")
            print("6- Remove Song")
            print("7- Back")

            while True:
                n = int(input("Enter Your Choice: "))
                if n == 1:
                    # TODO: Play song
                    song_name = input("Enter the song name: ")
                    url = self.play_song(song_name)
                    play.play(url)
                    break
                elif n == 2:
                    # TODO: close song
                    play.close()
                    break
                elif n == 3:
                    # TODO: Play playlist
                    break
                elif n == 4:
                    self.order_songs_by(id)
                    return
                elif n == 5:
                    self.add_song(id)
                    break
                elif n == 6:
                    self.remove_song(id)
                    break
                elif n == 7:
                    return
                else:
                    print("INVALID NUMBER")

    def add_playlist(self):
        name = input("Enter name: ")
        description = input("Enter Description: ")
        self._db.add_playlist(name, description)

    def order_songs_by(self, id):
        while True:
            print("\n1- Band Name ")
            print("2- Song Name")
            print("3- Song Release")
            print("4- Song Length")
            print("5- Back")
            while True:
                n = int(input("Enter Your Choice: "))
                if n == 1:
                    self.view_playlist(id, "bandName")
                    return
                elif n == 2:
                    self.view_playlist(id, "songName")
                    return
                elif n == 3:
                    self.view_playlist(id, "songRelease")
                    return
                elif n == 4:
                    self.view_playlist(id, "songLength")
                    return
                elif n == 5:
                    return
                else:
                    print("INVALID NUMBER")

    def add_song(self, playlist_id):
        self.print_title("All Songs")
        songs = self._db.get_all_songs()
        headers = ["Song Name", "Song Length", "Song URL", "Release Date", "Band"]
        self.print_attrs(headers, songs)
        url = input("Enter URL: ")
        self._db.add_song_to_playlist(playlist_id, url)

    def remove_song(self, playlist_id):
        url = input("Enter URL: ")
        self._db.remove_song_from_playlist(playlist_id, url)

    def play_song(self, song_name):
        # TODO: complete function
        # songs_list = self._db.get_song_by_url(url)
        url = self._db.get_url_song_by_name(song_name)
        return url