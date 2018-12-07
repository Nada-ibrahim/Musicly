import queue
import threading
import winsound

def play(song):
    winsound.PlaySound(song, winsound.SND_ASYNC)

def close():
    winsound.PlaySound(None, winsound.SND_PURGE)


class Player:
    def __init__(self):
        self.q = queue.Queue()

    def play_multiple_songs(self, songs):
        for song in songs:
            self.q.put(song.url)
        t = threading.Thread(target=self.player)
        t.daemon = True
        t.start()

    def player(self):
        while True:
            sound = self.q.get()
            winsound.PlaySound(sound, winsound.SND_PURGE)


    def close_all_songs(self):
        with self.q.mutex:
            self.q.queue.clear()


