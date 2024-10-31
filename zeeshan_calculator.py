import math
import random

def calculator():
    calculator_version = "2.0"
    print("Welcome to Zeeshan's Calculator!")
    print("This is currently a work in progress.")
    name = input("Enter your name, please: ")
    print(f"Hello {name}!\nI hope you enjoy using this calculator :)")

    # Available operations in the calculator
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero",
        "powers": lambda x, y: x ** y,
        "sqrt": lambda x: math.sqrt(x) if x >= 0 else "Error: Negative input for square root",
        "percent": lambda x: x / 100,
        "pi": lambda: math.pi,
        "e": lambda: math.e,
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "log": lambda x, base=10: math.log(x, base) if x > 0 else "Error: Non-positive input for logarithm",
        "rand": lambda: random.random(),
        "randint": lambda x, y: random.randint(int(x), int(y)) if x <= y else "Error: Invalid range for randint"
    }

    # Display available commands
    def show_options():
        print("\nOptions:")
        for operation in operations:
            print(f"Enter '{operation}' for {operation} operation")
        print("Enter 'info' for more information")
        print("Enter 'name' to change your saved name")
        print("Enter 'quit' to exit")

    # Handles user commands
    def execute_command(command):
        if command == "quit":
            print(f"\nThank you for using this calculator, {name}!")
            return False

        elif command == "info":
            print(f"\nInformation:\nYour name is '{name}'\nCurrent version: {calculator_version}")
            return True

        elif command == "name":
            nonlocal name
            name = input("Enter your new name, please: ")
            print(f"Name updated to {name}")
            return True

        # Execute the mathematical operation if available
        elif command in operations:
            try:
                if command in {"add", "subtract", "multiply", "divide", "powers", "randint"}:
                    x = float(input("Enter the first number: "))
                    y = float(input("Enter the second number: "))
                    result = operations[command](x, y)
                elif command in {"sqrt", "percent", "sin", "cos", "tan", "log"}:
                    x = float(input("Enter the number: "))
                    base = float(input("Enter the base (default is 10): ")) if command == "log" else None
                    result = operations[command](x) if command != "log" else operations[command](x, base)
                else:
                    result = operations[command]()

                print(f"\nThe answer is {result}")
            except (ValueError, TypeError):
                print("Error: Invalid input")
            return True

        else:
            print("Unknown command")
            return True

    show_options()

    # Loop until the user quits
    while True:
        user_input = input("\nPlease input your command: ").lower()
        if not execute_command(user_input):
            break
        show_options()


# Run the calculator
calculator()
