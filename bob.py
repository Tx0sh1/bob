import datetime
from functions.music_player import music_player
from functions.calculator import calculate
from functions.weather import weather
from functions.movies import info
from functions.jokes import jokes

def greet_user():
    name = input("Hello there i am Bob, your personal basic assistant, What may I call you?: ")
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
        elif command == "jokes":
            jokes()
        elif command == "calculate":
            calculate()
        elif command == "movie":
            info()
        elif command == "weather":
            weather()
        elif command == "exit":
            break
        else:
            print("Unknown command. Please enter time, music, calculate or exit")

if __name__ == "__main__":
    main()