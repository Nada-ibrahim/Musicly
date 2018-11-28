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