import pygame
from tkinter import *

root = ""
list_of_songs = []
counter = 0


def work():
    music()
    root.mainloop()


def get_music(songs):
    global counter, list_of_songs, root
    counter = 0
    list_of_songs = []
    root = Tk()

    for song in songs:
        list_of_songs.append(song)
    work()


def music():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(list_of_songs[counter])
    pygame.mixer.music.play(0)
    queue()


def queue():
    global list_of_songs, counter
    busy = pygame.mixer.music.get_busy()
    if busy == FALSE:
        counter += 1
        if counter < len(list_of_songs):
            pygame.mixer.music.load(list_of_songs[counter])
            pygame.mixer.music.play(0)

    root.after(1, queue)


def close():
    pygame.mixer.music.stop()