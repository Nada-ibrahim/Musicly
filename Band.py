from typing import List

import Artist


class Band:
    #artists: List[Artist]

    def __init__(self, name, artists):
        self.artists = artists
        self.name = name
