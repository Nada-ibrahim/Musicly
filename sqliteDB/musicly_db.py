import sqlite3
from operator import itemgetter
from Song import Song
from Playlist import Playlist
from Artist import Artist
from Album import Album
import datetime


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
        self.add_band("Cairokee")
        # self.add_artist(Artist("Amir", "3-9-1234"))
        self.add_artist(Artist("Amr Diab", "3-9-1234"))
        self.add_artist_to_band("Cairokee", "Amir")

        self.add_playlist("myPlayList", "my favourite cairoke songs", 1)

        self.add_album("Cairokee", "No2ta beda")

        self.add_song("songGenre", "songURL", 1, "Cairokee", "layla", "release", "lyrics", 3)
        self.add_song_to_playlist(1, "songURL")

        self.add_song("songGenre2", "songURL2", 1, "Cairokee", "ed7ak", "release2", "lyrics2", 4)
        self.add_song_to_playlist(1, "songURL2")

    # Band Requester

    def add_band(self, band_name):
        cursor = self.con.cursor()
        query = ''' INSERT INTO Band( bandName ) VALUES ( ? ) '''

        try:
            cursor.execute(query, (band_name,))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        self.con.commit()

    def add_artist_to_band(self, band_name, artist_name):
        cursor = self.con.cursor()
        query = ''' INSERT INTO BandContainsArtists( bandName, artistName) VALUES ( ?, ? ) '''

        try:
            cursor.execute(query, (band_name, artist_name))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        self.con.commit()

    # Playlist Requester

    def add_playlist(self, name, description, play_list_id):

        cursor = self.con.cursor()
        query = ''' INSERT INTO Playlist( playlistName, playlistDescription, playlistID) VALUES ( ?,?,? ) '''

        try:
            cursor.execute(query, (name, description, play_list_id))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

    def add_song_to_playlist(self, playlist_id, song_url):
        cursor = self.con.cursor()
        query = ''' INSERT INTO PlaylistContainsSong( playlistID, songURL ) VALUES ( ?,? ) '''
        try:
            cursor.execute(query, (playlist_id, song_url))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        self.con.commit()

    def remove_song_from_playlist(self, playlist_id, song: Song):
        cursor = self.con.cursor()
        query = '''DELETE FROM PlaylistContainsSong WHERE playlistID = ? AND songURL = ?'''
        cursor.execute(query, (playlist_id, song.url))
        self.con.commit()

    def get_playlist_name_by_id(self, playlist_id):
        cursor = self.con.cursor()
        query = '''SELECT playlistName FROM Playlist WHERE playlistID = ?'''
        cursor.execute(query, (playlist_id,))
        self.con.commit()
        playlist_name = cursor.fetchall()
        return playlist_name[0][0]

    def get_all_playlists(self):
        cursor = self.con.cursor()
        query = '''SELECT playlistID, count(*) FROM PlaylistContainsSong GROUP BY playlistID'''
        cursor.execute(query)
        self.con.commit()
        playlist_number_of_songs = cursor.fetchall()

        playlist_name_id_songs = [[self.get_playlist_name_by_id(item[0])] + list(item) for item in
                                  playlist_number_of_songs]
        return playlist_name_id_songs

    def get_playlist_information(self, playlist_id, ordered_by, ascending):
        cursor = self.con.cursor()
        query = '''SELECT playlistName, playlistDescription FROM Playlist WHERE playlistID = ?'''
        cursor.execute(query, (playlist_id,))
        self.con.commit()

        playlist_info = cursor.fetchall()
        playlist = Playlist(*playlist_info[0])

        query = '''SELECT PlaylistContainsSong.songURL, songName, songLength
                    FROM PlaylistContainsSong
                    INNER JOIN Song ON Song.songURL = PlaylistContainsSong.songURL
                    WHERE playlistID = ?
                    ORDER BY ''' + ordered_by + ''' ''' + ascending

        cursor.execute(query, (playlist_id,))
        old_songs_list = cursor.fetchall()

        for item in old_songs_list:
            song = Song(url=item[0], name=item[1], length=item[2])
            playlist.add_song(song)

        return playlist

    def delete_playlist(self, playlist_id):
        cursor = self.con.cursor()
        query = ''' DELETE FROM Playlist WHERE playlistID = ? '''
        cursor.execute(query, (playlist_id,))
        self.con.commit()

    # Song Requester

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

    def get_song_info(self, song_name):

        cursor = self.con.cursor()
        query = ''' SELECT * FROM Song WHERE songName = ? '''
        cursor.execute(query, (song_name,))
        songs_list = cursor.fetchall()
        self.con.commit()

        new_songs_list = []
        for item in songs_list:
            song = Song(*item)
            new_songs_list.append(song)

        return new_songs_list

    def get_all_songs(self):
        cursor = self.con.cursor()
        query = ''' SELECT * FROM Song '''
        cursor.execute(query)
        songs_list = cursor.fetchall()
        self.con.commit()

        new_songs_list = []
        for item in songs_list:
            song = Song(*item)
            new_songs_list.append(song)

        return new_songs_list

    def remove_song(self, song_name):
        cursor = self.con.cursor()
        query = ''' DELETE FROM Song WHERE songName = ? '''
        cursor.execute(query, (song_name,))
        self.con.commit()

    def get_band_songs(self, band_name):
        cursor = self.con.cursor()
        query = ''' SELECT songURL, songName, songLength FROM Song WHERE bandName = ? '''
        cursor.execute(query, (band_name,))
        songs_list = cursor.fetchall()
        self.con.commit()

        new_songs_list = []
        for item in songs_list:
            song = Song(url=item[0], name=item[1], length=item[2])
            new_songs_list.append(song)

        return new_songs_list

    def get_artist_songs(self, artist_name):
        cursor = self.con.cursor()
        query = ''' SELECT bandName FROM BandContainsArtists WHERE  artistName = ?'''
        cursor.execute(query, (artist_name,))
        bands_names = cursor.fetchall()
        self.con.commit()

        artist_songs = []
        for band_name in bands_names:
            artist_songs += self.get_band_songs(band_name[0])

        return artist_songs

    def get_song_by_url(self, URL):
        cursor = self.con.cursor()
        query = ''' SELECT songURL, songName, songLength FROM Song WHERE songURL = ? '''
        cursor.execute(query, (URL,))
        songs_list = cursor.fetchall()
        self.con.commit()

        new_songs_list = []
        for item in songs_list:
            song = Song(url=item[0], name=item[1], length=item[2])
            new_songs_list.append(song)

        return new_songs_list

    def get_genre_songs(self, genre_name):
        cursor = self.con.cursor()
        query = ''' SELECT songURL FROM SongGenres WHERE songGenre = ?'''
        cursor.execute(query, (genre_name,))
        songs_URLs = cursor.fetchall()
        self.con.commit()

        songs = []
        for song_URL in songs_URLs:
            songs += self.get_song_by_url(song_URL[0])

        return songs

    # Album Requester

    def add_album(self, band_name, album_title=""):

        cursor = self.con.cursor()
        query = ''' INSERT INTO Album( bandName, albumTitle ) VALUES ( ?,? ) '''

        try:
            cursor.execute(query, (band_name, album_title))
        except sqlite3.IntegrityError as e:
            print("was already stored in table ")

        self.con.commit()

    def get_album_title_by_id(self, album_id):
        cursor = self.con.cursor()
        query = '''SELECT albumTitle FROM Album WHERE albumID = ?'''
        cursor.execute(query, (album_id,))
        self.con.commit()
        album_title = cursor.fetchall()
        return album_title[0][0]

    def get_all_albums(self):
        cursor = self.con.cursor()
        query = '''SELECT albumID, count(*) FROM Song GROUP BY albumID'''
        cursor.execute(query)
        self.con.commit()
        album_number_of_songs = cursor.fetchall()

        album_title_id_songs = [[self.get_album_title_by_id(item[0])] + list(item) for item in
                                album_number_of_songs]
        return album_title_id_songs  # list of lists, not list of tuples

    def get_album_information(self, album_id, ordered_by, ascending):
        cursor = self.con.cursor()
        query = '''SELECT albumTitle, bandName FROM Album WHERE albumID = ?'''
        cursor.execute(query, (album_id,))
        self.con.commit()

        album_info = cursor.fetchall()
        album = Album(*album_info[0])

        query = '''SELECT songURL, songName, songLength 
                   FROM Song 
                   WHERE albumID = ?
                   ORDER BY ''' + ordered_by + ''' ''' + ascending
        cursor.execute(query, (album_id))
        self.con.commit()
        songs_list = cursor.fetchall()
        new_songs_list = []

        album.songs_number = len(songs_list)
        for item in songs_list:
            song = Song(url=item[0], name=item[1], length=item[2])
            new_songs_list.append(song)
        return album, songs_list

    def delete_album(self, album_title):
        cursor = self.con.cursor()
        query = ''' DELETE FROM Album WHERE albumTitle = ? '''
        cursor.execute(query, (album_title,))
        self.con.commit()

    # Artist Requester

    def add_artist(self, artist: Artist):
        cursor = self.con.cursor()
        query = '''INSERT INTO Artist( artistName, dateBirth ) VALUES ( ?,? )'''

        try:
            cursor.execute(query, (artist.name, artist.date_of_birth))
        except:
            print("was already stored in table ")

    def get_all_Artists(self):
        cursor = self.con.cursor()
        query = '''SELECT Artist.artistName, dateBirth, bandName
                   FROM Artist
                   INNER JOIN BandContainsArtists ON BandContainsArtists.artistName = Artist.artistName'''
        cursor.execute(query)
        artists_list = cursor.fetchall()
        self.con.commit()

        new_artists_list = []
        bands_list = []
        for item in artists_list:
            artist = Artist(item[0], item[1])
            new_artists_list.append(artist)
            bands_list.append(item[2])

        return new_artists_list, bands_list

    def remove_artist(self, artist_name):
        cursor = self.con.cursor()
        query = ''' DELETE FROM Artist WHERE artistName = ? '''
        cursor.execute(query, (artist_name,))
        self.con.commit()
