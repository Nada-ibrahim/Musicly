import sqlite3


class MusiclyDB:

    def __init__(self):
        self.con = self.create_connection()
        self.create_tables()
        self.fill_db()

    def create_connection(self):
        self.con = sqlite3.connect("musicly.db")
        return self.con

    def create_tables(self):
        cursor = self.con.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Playlist (
                              playlistID INTEGER PRIMARY KEY NOT NULL, 
                              playlistName VARCHAR(100) NOT NULL,
                              playlistDescription VARCHAR(200)
                            );
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Album (
                              albumID    INTEGER PRIMARY KEY NOT NULL, 
                              bandName   VARCHAR(100) NOT NULL, 
                              albumTitle VARCHAR(100) NOT NULL
                            );
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Band (
                              bandName VARCHAR(100) PRIMARY KEY NOT NULL
                            );
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Artist (
                              artistName VARCHAR(100) PRIMARY KEY NOT NULL, 
                              dateBirth  DATE
                            );
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Song (
                              songURL     VARCHAR(200) PRIMARY KEY NOT NULL, 
                              albumID     INTEGER NOT NULL,
                              bandName    VARCHAR(100) NOT NULL,  
                              songName    VARCHAR(100) UNIQUE NOT NULL,
                              songRelease DATE         ,
                              songLyrics  VARCHAR(200) ,
                              songLength  INTEGER      
                            );
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS SongGenres (
                              songURL      VARCHAR(200) NOT NULL, 
                              songGenre    VARCHAR(100) NOT NULL,
                              PRIMARY KEY (songURL, songGenre)
                            );
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS PlaylistContainsSong (
                              playlistID INTEGER NOT NULL, 
                              songURL    VARCHAR(200) NOT NULL, 
                              PRIMARY KEY (playlistID, songURL)
                            );
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS BandContainsArtists (
                              bandName   VARCHAR(100) NOT NULL, 
                              artistName VARCHAR(100) NOT NULL,
                              PRIMARY KEY (bandName, artistName)
                            );
                       ''')
        self.con.commit()

    def fill_db(self):
        self.add_song("genre1", "url1", 1, "Nero", "song1", "", "", 0)
        self.add_song("genre2", "url2", 1, "Nero", "song2", "", "", 0)
        self.add_playlist("Esmaan", "", "url1", 1)
        self.add_playlist("Dari Ya Alby", "", "url2", 2)
        self.add_artist("Nayra", "")
        self.add_band("Nero", "Nayra")
        self.add_album("Nero", "You are amazing")

    def add_playlist(self, name, description, song_url, playlist_id):

        cursor = self.con.cursor()
        query = ''' INSERT INTO Playlist( playlistName, playlistDescription ) VALUES ( ?,? ) '''

        try:
            cursor.execute(query, (name, description))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        query = ''' INSERT INTO PlaylistContainsSong( playlistID, songURL ) VALUES ( ?,? ) '''

        try:
            cursor.execute(query, (playlist_id, song_url))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        self.con.commit()

    def add_album(self, band_name, album_title=""):

        cursor = self.con.cursor()
        query = ''' INSERT INTO Album( bandName, albumTitle ) VALUES ( ?,? ) '''

        try:
            cursor.execute(query, (band_name, album_title))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        self.con.commit()

    def add_band(self, band_name, artist_name):

        cursor = self.con.cursor()
        query = ''' INSERT INTO Band( bandName ) VALUES ( ? ) '''

        try:
            cursor.execute(query, (band_name,))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        query = ''' INSERT INTO BandContainsArtists( bandName, artistName) VALUES ( ?, ? ) '''

        try:
            cursor.execute(query, (band_name, artist_name))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        self.con.commit()

    def add_artist(self, artist_name, date_birth):

        cursor = self.con.cursor()
        query = ''' INSERT INTO Artist( artistName, dateBirth ) VALUES ( ?, ? ) '''

        try:
            cursor.execute(query, (artist_name, date_birth))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        self.con.commit()

    def add_song(self, song_genre, song_url, album_id, band_name, song_name, song_release, song_lyrics,
                 song_length):

        cursor = self.con.cursor()
        query = ''' INSERT INTO Song( songURL, albumID, bandName, songName, songRelease, songLyrics, songLength ) 
                    VALUES ( ?, ?, ?, ?, ?, ?, ? ) '''

        try:
            cursor.execute(query,
                           (song_url, album_id, band_name, song_name, song_release, song_lyrics, song_length))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        query = ''' INSERT INTO SongGenres( songURL, songGenre ) 
                    VALUES ( ?, ? ) '''
        try:
            cursor.execute(query, (song_url, song_genre))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        self.con.commit()
