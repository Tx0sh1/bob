import datetime
from music_player import music_player
from calculator import calculate

def greet_user():
    name = input("Hello there, What may I call you?: ")
    print(f"Welcome to your personal assistant, {name}!")

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    greet_user()
    while True:
        command = input("How may I be of service today?: ").lower()
        if command == "time":
            print(f"Current time: {get_current_time()}")
        elif command == "music":
            music_player()
        elif command == "calculate":
            calculate()
        elif command == "exit":
            break
        else:
            print("Unknown command. Please enter time, music, calculate or exit")

if __name__ == "__main__":
    main()