import pygame

def music_player():
    pygame.init()
    pygame.mixer.init()

    def load_song():
        pygame.mixer.music.load('FILE PATH')

    def play_song():
        pygame.mixer.music.play()

    def pause():
        pygame.mixer.music.pause()

    def rewind():
        pygame.mixer.music.rewind()

    def stop():
        pygame.mixer.music.stop()

    while True:
        buttons = input("Type in: Play/Pause/Rewind/Stop: ").lower()
        load_song()
        if buttons == "play":
            play_song()
        elif buttons == "pause":
            pause()
        elif buttons == "rewind":
            rewind()
        elif buttons == "stop":
            stop()
            break
