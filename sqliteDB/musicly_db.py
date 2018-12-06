import sqlite3
from pathlib import Path

from Song import Song
from Playlist import Playlist
from Artist import Artist
from Album import Album


class MusiclyDB:

    def __init__(self):
        path = Path("musicly.db")
        if not path.exists():
            self.con = self.create_connection()
            self.create_tables()
            self.fill_db()
        self.con = self.create_connection()

    def create_connection(self):
        self.con = sqlite3.connect("musicly.db")
        return self.con

    def create_tables(self):
        cursor = self.con.cursor()

        cursor.execute(''' CREATE TABLE IF NOT EXISTS Playlist (
                            playlistID INTEGER PRIMARY KEY NOT NULL, 
                            playlistName VARCHAR(100) NOT NULL,
                            playlistDescription VARCHAR(200));
                       ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Album (
                            albumID    INTEGER PRIMARY KEY NOT NULL, 
                            bandName   VARCHAR(100) NOT NULL, 
                            albumTitle VARCHAR(100) NOT NULL,

                            CONSTRAINT fk_BandName_Album
                            FOREIGN KEY (bandName)
                            REFERENCES Band(bandName)
                            ON DELETE CASCADE   
                            );
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Band (
                            bandName VARCHAR(100) PRIMARY KEY NOT NULL);
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Artist (
                          artistName VARCHAR(100) PRIMARY KEY NOT NULL, 
                          dateBirth  DATE);
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Song (
                            songURL            VARCHAR(200) PRIMARY KEY NOT NULL, 
                            albumID            INTEGER NOT NULL,
                            bandName           VARCHAR(100) NOT NULL,  
                            featured_artist    VARCHAR(100) NOT NULL,  
                            songName           VARCHAR(100) UNIQUE NOT NULL,
                            songRelease        DATE         ,
                            songLyrics         VARCHAR(200) ,
                            songLength         VARCHAR(100) ,
                              
                            FOREIGN KEY(bandName, featured_artist)  REFERENCES Band(bandName, featured_artist),

                            CONSTRAINT fk_AlbumID_Song
                            FOREIGN KEY (albumID)
                            REFERENCES Album(albumID)
                            ON DELETE CASCADE
                             );
                        ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS SongGenres (
                            songURL      VARCHAR(200) NOT NULL, 
                            songGenre    VARCHAR(100) NOT NULL,
                            PRIMARY KEY (songURL, songGenre),
                            CONSTRAINT fk_Song_Genres
                            FOREIGN KEY (songURL)
                            REFERENCES Song(songURL)
                            ON DELETE CASCADE
                            );
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS PlaylistContainsSong (
                            playlistID INTEGER NOT NULL, 
                            songURL    VARCHAR(200) NOT NULL, 
                            PRIMARY KEY (playlistID, songURL),
                            CONSTRAINT fk_Song_Playlist
                            FOREIGN KEY (songURL)
                            REFERENCES Song(songURL)
                            ON DELETE CASCADE
                            );
                       ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS BandContainsArtists (
                            bandName   VARCHAR(100) NOT NULL, 
                            artistName VARCHAR(100) NOT NULL,
                            PRIMARY KEY (bandName, artistName),
                            CONSTRAINT fk_Artist_Band
                            FOREIGN KEY (artistName)
                            REFERENCES Artist(artistName)
                            ON DELETE CASCADE
                            );
                       ''')
        self.con.commit()

    def fill_db(self):
        self.add_band("Cairokee")
        self.add_artist(Artist("Amir", "3-9-1234"))
        self.add_artist(Artist("Amr Diab", "3-9-1234"))
        self.add_artist_to_band("Cairokee", "Amir")

        self.add_playlist("myPlayList", "my favourite cairoke songs")

        self.add_album("Cairokee", "No2ta beda")

        self.add_song("songGenre", "songURL", 1, "Cairokee", "",  "layla", "release", "lyrics", 3)
        self.add_song_to_playlist(1, "songURL")

        self.add_song("songGenre2", "songURL2", 1, "Cairokee", "", "ed7ak", "release2", "lyrics2", 4)
        self.add_song_to_playlist(1, "songURL2")

        '''Michael Jackson'''
        self.add_band("Jackson")
        self.add_artist(Artist("Michael Jackson", "29-8-1958"))
        self.add_artist_to_band("Jackson", "Michael Jackson")

        self.add_playlist("Thriller", "Thriller is the sixth studio album by American singer Michael Jackson, "
                                      "released on November 30, 1982, in the United States")

        self.add_album("Jackson", "Thriller")

        self.add_song("Post-disco", "Michael Jackson/Thriller/01. Wanna be startin' somethin'.wav", 2, "Jackson", "", "Wanna be startin' somethin'", "8-5-1983",
                      "I said you wanna be startin' somethin'"
                      "You got to be startin' somethin' "
                      "I said you wanna be startin' somethin'"
                      "You got to be startin' somethin'"
                      "It's too high to get over (yeah, yeah)"
                      "Too low to get under (yeah, yeah)"
                      "You're stuck in the middle (yeah, yeah)"
                      "And the pain is thunder (yeah, yeah)"
                      "It's too high to get over (yeah, yeah)"
                      "Too low to get under (yeah, yeah)"
                      "You're stuck in the middle (yeah, yeah)"
                      "And the pain is thunder (yeah, yeah)", 6)
        self.add_song_to_playlist(2, "Michael Jackson/Thriller/01. Wanna be startin' somethin'.wav")

        self.add_song("Post-disco", "Michael Jackson/Thriller/03. Thriller.wav", 2, "Jackson", "", "Thriller", "2-11-1983",
                      "It's close to midnight "
                      "Something evil's lurking from the dark"
                      "Under the moonlight"
                      "You see a sight that almost stops your heart"
                      "You try to scream"
                      "But terror takes the sound before you make it"
                      "You start to freeze"
                      "As horror looks you right between your eyes"
                      "You're paralyzed", 6)

        self.add_song_to_playlist(2, "Michael Jackson/Thriller/03. Thriller.wav")

        self.add_song("Hard rock", "Michael Jackson/Thriller/04. Beat It.wav", 2, "Jackson", "", "Beat It", "14-2-1983",
                      "They told him don't you ever come around here"
                      "Don't want to see your face, you better disappear"
                      "The fire's in their eyes and their words are really clear"
                      "So beat it, just beat it", 5)
        self.add_song_to_playlist(2, "Michael Jackson/Thriller/04. Beat It.wav")

        '''Eagles'''
        self.add_band("Eagles")
        self.add_artist(Artist("Don Henley", "22-5-1947"))
        self.add_artist(Artist("Joe Walsh", "20-11-1947"))
        self.add_artist(Artist("Timothy B. Schmit", "30-10-1947"))
        self.add_artist_to_band("Don Henley", "Eagles")
        self.add_artist_to_band("Joe Walsh", "Eagles")
        self.add_artist_to_band("Timothy B. Schmit", "Eagles")

        self.add_playlist("Their Greatest Hits", "Their Greatest Hits (1971–1975) is the first compilation album by "
                                                 "the Eagles, released in 1976. The album contains a selection of "
                                                 "songs from the Eagles' first four albums released in the period "
                                                 "from the Eagles' formation in 1971 up to 1975. It was the "
                                                 "best-selling album of the 20th century in the United States")

        self.add_album("Eagles", "Their Greatest Hits")

        self.add_song("Country rock", "Eagles/Their Greatest Hits/01. Take It Easy.wav", 3, "Eagles", "",
                      "Take It Easy", "1-5-1972",
                      "Take It easy, take it easy"
                      "Don't let the sound of your own wheels"
                      "Drive you crazy"
                      "Lighten up while you still can"
                      "Don't even try to understand"
                      "Just find a place to make your stand"
                      "And take it easy", 4)
        self.add_song_to_playlist(3, "Eagles/Their Greatest Hits/01. Take It Easy.wav")

        self.add_song("Country rock", "Eagles/Their Greatest Hits/02. Already Gone.wav", 3, "Eagles", "",
                      "Already Gone", "19-4-1974",
                      "Well, I heard some people talkin' just the other day "
                      "And they said you were gonna put me on a shelf "
                      "But let me tell you I got some news for you "
                      "And you'll soon find out it's true "
                      "And then you'll have to eat your lunch all by yourself '"
                      "Cause I'm already gone "
                      "And I'm feelin' strong "
                      "I will sing this vict'ry song "
                      "Woo hoo hoo, my my, woo hoo hoo"
                      "", 4)
        self.add_song_to_playlist(3, "Eagles/Their Greatest Hits/02. Already Gone.wav")

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

    def add_playlist(self, name, description):

        cursor = self.con.cursor()
        query = ''' INSERT INTO Playlist( playlistName, playlistDescription) VALUES (?,?) '''

        try:
            cursor.execute(query, (name, description))
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

    def remove_song_from_playlist(self, playlist_id, url):
        cursor = self.con.cursor()
        query = '''DELETE FROM PlaylistContainsSong WHERE playlistID = ? AND songURL = ?'''
        cursor.execute(query, (playlist_id, url))
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
        query = '''SELECT Playlist.playlistID, playlistName, count(*)
                    FROM Playlist
                    LEFT JOIN PlaylistContainsSong ON PlaylistContainsSong.playlistID = Playlist.playlistID
                    GROUP BY Playlist.playlistID'''
        cursor.execute(query)
        self.con.commit()
        list1 = cursor.fetchall()

        query = '''SELECT playlistID
                   FROM PlaylistContainsSong
                   GROUP BY playlistID
                            '''
        cursor.execute(query)
        list2 = cursor.fetchall()
        self.con.commit()

        for i in range(len(list1)):
            if list1[i][2] == 1 and not list2.__contains__(list1[i][1]):
                list1[i] = list1[i][:2] + (0,)

        return list1


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

    def add_song(self, song_genre, song_url, album_id, band_name, featured_artist, song_name, song_release, song_lyrics,
                 song_length):

        cursor = self.con.cursor()
        query = ''' INSERT INTO Song( songURL, albumID, bandName, featured_artist, songName, songRelease, songLyrics, songLength ) 
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ? ) '''

        try:
            cursor.execute(query,
                           (song_url, album_id, band_name, featured_artist, song_name, song_release, song_lyrics, song_length))
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

    def get_url_song_by_name(self, song_name):
        cursor = self.con.cursor()
        query = ''' SELECT songURL FROM Song WHERE songName = ? '''
        cursor.execute(query, (song_name,))
        url = cursor.fetchall()
        self.con.commit()
        return url[0][0]

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
        query = ''' SELECT * FROM Song WHERE songURL = ? '''
        cursor.execute(query, (URL,))
        songs_list = cursor.fetchall()
        self.con.commit()

        new_songs_list = []
        for item in songs_list:
            song = Song(url=item[0], album=item[1],
                        band=item[2], featured_artist=item[3],
                        name=item[4], release_date=item[5],
                        lyrics=item[6], length=item[7])
            new_songs_list.append(song)

        return new_songs_list[0]

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

    def get_album_information(self, album_id):
        cursor = self.con.cursor()
        query = '''SELECT albumTitle, bandName FROM Album WHERE albumID = ?'''
        cursor.execute(query, (album_id,))
        self.con.commit()

        album_info = cursor.fetchall()
        album = Album(*album_info[0])

        query = '''SELECT songURL, songName, songLength 
                   FROM Song 
                   WHERE albumID = ?'''
        cursor.execute(query, (album_id))
        self.con.commit()
        songs_list = cursor.fetchall()

        for item in songs_list:
            song = Song(url=item[0], name=item[1], length=item[2])
            album.add_song(song)
        return album

    def delete_album(self, album_id):
        cursor = self.con.cursor()
        query = ''' DELETE FROM Album WHERE albumID = ? '''
        cursor.execute(query, (album_id,))
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
            temp = []; temp.append(item[2])
            bands_list.append(temp)

        return new_artists_list, bands_list

    def remove_artist(self, artist_name):
        cursor = self.con.cursor()
        query = ''' DELETE FROM Artist WHERE artistName = ? '''
        cursor.execute(query, (artist_name,))
        self.con.commit()
