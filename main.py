from sqliteDB.musicly_db import MusiclyDB
from ui.welcome_page import WelcomePage

db = MusiclyDB()
welcome = WelcomePage(db)
# song = SongRequester(db)

# db.get_all_songs()
# db.get_artist_songs("Nayra")
# db.get_band_songs("Nero")
# song.get_song_information("song1")
# song.remove_song("song1")
# print(db.get_all_songs())
# db.get_all_Artists()
# db.get_playlist_information(1, "songName", "ASC")
# db.get_song_info("ed7ak")
# print(db.get_artist_songs("Amir"))
# print(db.get_all_Artists())