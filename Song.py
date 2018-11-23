from datetime import date
import Album
import Band


class Song:
    band: Band
    featured_artist: Band
    album: Album
    release_date: date

    def __init__(self, name="", band=None, featured_artist=None, album=None,
                 release_date=None, genres=
                 None, lyrics="", length="", url=""):
        self.url = url
        self.length = length
        self.lyrics = lyrics
        self.genres = genres
        self.release_date = release_date
        self.album = album
        self.featured_artist = featured_artist
        self.band = band
        self.name = name
