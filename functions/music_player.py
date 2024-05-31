import pygame

def music_player():
    pygame.init()
    pygame.mixer.init()

    music_file = input("Enter the file location: ")

    try:
        pygame.mixer.music.load(music_file)
    except pygame.error:
        print(f"Error: Could not load music file '{music_file}'.")
        return

    def play_song():
        pygame.mixer.music.play()

    def pause():
        pygame.mixer.music.pause()

    def rewind():
        pygame.mixer.music.rewind()

    def stop():
        pygame.mixer.music.stop()

    while True:
        action = input("Type in: Play/Pause/Rewind/Stop: ").lower()
        
        if action == "play":
            play_song()
        elif action == "pause":
            pause()
        elif action == "rewind":
            rewind()
        elif action == "stop":
            stop()
            break
