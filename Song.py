from datetime import date
import Album
import Band


class Song:
    band: Band
    featured_artist: Band
    album: Album
    release_date: date

    def __init__(self, url="", album=None, band=None, name="",
                 release_date=None, lyrics="", length="", featured_artist=None, genres=None):
        self.url = url
        self.length = length
        self.lyrics = lyrics
        self.genres = genres
        self.release_date = release_date
        self.album = album
        self.featured_artist = featured_artist
        self.band = band
        self.name = name
