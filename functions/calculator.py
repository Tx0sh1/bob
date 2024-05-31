def calculate():
    print("This is a simple calculator... for now")
    op = input("Input the operation (add, sub, multiply, division): ")
    n1 = float(input("Enter the first number here: "))
    n2 = float(input("Enter your 2nd number: "))
    if op == "add":
        print(n1 + n2)
    elif op == "sub" or "subtract":
        print(n1 - n2)
    elif op == "multiply":
        print(n1 * n2)
    elif op == "division":
        if n2 != 0:
            print(n1 / n2)
        else:
            print("Error: Division by zero is not allowed")
    else:
        print("Invalid operation. Please enter add, sub, multiply or division")