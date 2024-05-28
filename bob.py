import datetime
from playsound import playsound

def greet_user():
    name = input("Hello there, What may i call you?: ")
    print("Welcome to your personal assistant " + name)
def calculate():
    print("This is a simple calculator...for now")
    n1 = float(input("enter the first number here: "))
    n2 = float(input("enter your 2nd number: "))
    op = float(input("input the operation as add, sub, multiply or division: "))
    if op == "add":
        print(n1 + n2)
    elif op == "subtract":
        print(n1 - n2)
    elif op == "multiply":
        print(n1 * n2)
    elif op == "division":
        print(n1 / n2)
    else:
        print("Enter only numbers")
def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def music():
    playsound('e.mp3')

def main():
    greet_user()
    while True:
        command = input("How may i be of service today?: ")
        if command == "time":
            print("current time: ", get_current_time())
        elif command == "music":
            music()
        elif command == "calculate":
            calculate()
        elif command == "exit":
            break
        else:
            print("unknow command")
if __name__ == "__main__":
    main()