import winsound


def play(song):
    winsound.PlaySound(song, winsound.SND_ASYNC)


def close():
    winsound.PlaySound(None, winsound.SND_PURGE)