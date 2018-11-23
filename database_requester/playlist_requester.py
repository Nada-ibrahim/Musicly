import Playlist
import Song


class PlaylistRequester:
    def get_all_playlists(self):
        print()
        # TODO: get all playlists names with songs number from database

    def get_playlist_information(self, playlist_name, ordered_by, ascending):
        print()
        # TODO: get playlist description with their songs name and duration and URL ordered by an attribute

    def add_playlist(self, playlist: Playlist):
        print()
        # TODO: add playlist decription and name to database

    def delete_playlist(self, playlist_name):
        print()
        # TODO: delete playlist from database

    def add_song_to_playlist(self, playlist_name, song: Song):
        print()
        # TODO: add song to playlist in database

    def remove_song_from_playlist(self, playlist_name, Song_name):
        print()
        # TODO: remove song to playlist in database
