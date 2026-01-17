#Calculator Made by Team CSS

def addition(num1, num2):
    sum = num1 + num2
    print(f"\n\nThe sum of {num1} and {num2} is {sum}.\n\n")

while(True):
    print("This is a simple floating point integer calculator")
    print("Choices: ")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("\n\nWhat would you like to do? Input the number of the operation: "))

    match choice:
        case 1:
            num1 = float(input("Input the first number: "))
            num2 = float(input("Input the second number: "))
            addition(num1, num2)
            continue
        case 2:
            continue
        case 3:
            continue
        case 4:
            continue
        case _:
            print("Choice not found. Try again")
            continue
