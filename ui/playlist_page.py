from play_song.play import Player
from play_song import play_pygame
from ui.page import Page
from play_song import play


class PlaylistPage(Page):

    def __init__(self, db):
        super().__init__(db)
        self.player = Player()
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
                    self.view_playlist(id, order_by="songName")
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

    def view_playlist(self, id, order_by, ascending = "ASC"):
        while True:
            playlist = self._db.get_playlist_information(id, order_by, ascending)
            self.print_title(playlist.name)
            print(playlist.description)
            print()
            headers = ["Song Name", "Duration"]
            self.print_attrs(headers, playlist.songs)

            print("1- Play Song")
            print("2- Play Playlist")
            print("3- Sort by")
            print("4- Add Song")
            print("5- Remove Song")
            print("6- Back")

            while True:
                n = int(input("Enter Your Choice: "))
                if n == 1:
                    song_name = input("Enter the song name: ")
                    self.play_song(song_name)
                    break
                elif n == 2:
                    # TODO: Play playlist
                    # self.player.play_multiple_songs(playlist.songs)
                    play_pygame.get_music([song.url for song in playlist.songs])
                    break
                elif n == 3:
                    self.order_songs_by(id)
                    return
                elif n == 4:
                    self.add_song(id)
                    break
                elif n == 5:
                    self.remove_song(id)
                    break
                elif n == 6:
                    play_pygame.close()
                    return
                else:
                    print("INVALID NUMBER")

    def add_playlist(self):
        name = input("Enter name: ")
        description = input("Enter Description: ")
        self._db.add_playlist(name, description)

    def order_songs_by(self, id):
        while True:
            print("\n1- Name Ascending")
            print("2- Name Descending")
            print("3- Artist ")
            print("4- Album")
            print("5- Genre")
            print("6- Release Date")
            print("7- Back")
            while True:
                n = int(input("Enter Your Choice: "))
                if n == 1:
                    self.view_playlist(id, "songName")
                    return
                elif n == 2:
                    self.view_playlist(id, "songName", "DESC")
                    return
                elif n == 3:
                    self.view_playlist(id, "Song.bandName")
                    return
                elif n == 4:
                    self.view_playlist(id, "albumTitle")
                    return
                elif n == 5:
                    self.view_playlist(id, "songGenre")
                    return
                elif n == 6:
                    self.view_playlist(id, "songRelease")
                    return
                elif n == 7:
                    return
                else:
                    print("INVALID NUMBER")

    def add_song(self, playlist_id):
        self.print_title("All Songs")
        songs = self._db.get_all_songs()
        headers = ["Song Name", "Song Length", "Release Date", "Band"]
        self.print_attrs(headers, songs)
        song_name = input("Enter Name: ")
        url = self._db.get_url_song_by_name(song_name)
        self._db.add_song_to_playlist(playlist_id, url)

    def remove_song(self, playlist_id):
        song_name = input("Enter Name: ")
        url = self._db.get_url_song_by_name(song_name)
        self._db.remove_song_from_playlist(playlist_id, url)

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

