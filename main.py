from sqliteDB.musicly_db import MusiclyDB
from database_requester.song_requester import SongRequester

db = MusiclyDB()
song = SongRequester(db)

db.get_all_songs()
song.get_song_information("song1")
song.remove_song("song1")
db.get_all_songs()