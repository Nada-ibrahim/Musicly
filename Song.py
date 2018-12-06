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
        self.name = name
        self.length = length
        self.url = url
        self.release_date = release_date
        self.band = band
        self.album = album
        self.lyrics = lyrics
        self.genres = genres
        self.featured_artist = featured_artist

