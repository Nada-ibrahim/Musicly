import sqlite3
with sqlite3.connect("musicly.db") as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Playlist (
                  playlistID INTEGER PRIMARY KEY NOT NULL, 
                  playlistName VARCHAR(100) NOT NULL,
                  playlistDescription VARCHAR(200)
                  );
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Album (
                  bandName   VARCHAR(100) NOT NULL, 
                  albumID    INTEGER PRIMARY KEY NOT NULL, 
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
                  albumID     INTEGER NOT NULL,
                  bandName   VARCHAR(100) NOT NULL,  
                  songURL     VARCHAR(200) PRIMARY KEY NOT NULL, 
                  songName    VARCHAR(100) NOT NULL,
                  songRelease DATE         NOT NULL,
                  songLyrics  VARCHAR(200) NOT NULL,
                  songLength  INTEGER      NOT NULL
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