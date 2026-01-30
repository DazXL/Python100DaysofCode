# Task 5 is the Calculator Challenge

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# defining the operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# the keys in the dictionary calls the operation functions above as values
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Logic
def calculator():
    print(logo)
    should_accumulate = True
    num1 = int(input("Enter first number: "))

    while should_accumulate:
        for symbol in operators:
            print(symbol)
        operation = input("Enter operation: ")
        num2 = int(input("Enter second number: "))
        answer = operators[operation](num1, num2) # calling the operation function using the dictionary
        print(f"{num1} {operation} {num2} = {answer}")

        choice = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: (y/n)")

        if choice == "y":
                num1 = answer #saves the number to loop and calculate with another number

        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() #recursion to restart the calculator

calculator() #kickstart the code
