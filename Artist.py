from datetime import date


class Artist:
    date_of_birth: date

    def __init__(self, name, date_of_birth):
        self.date_of_birth = date_of_birth
        self.name = name
