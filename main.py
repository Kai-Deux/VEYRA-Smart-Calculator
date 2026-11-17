
# VEYRA Digital Studio
# Project: Smart Calculator
# Version: 1.0

from calculator import add, subtract, multiply, divide
from validation import get_valid_number



def display_menu():
    """Display the available calculator operations."""
    print("\n" + "=" * 40)
    print("       VEYRA SMART CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=" * 40)


def main():
    while True:
        display_menu()

        choice = input("Select an option (1-5): ")

        if choice == "5":
            print("Thank you for using VEYRA Smart Calculator.")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Please try again.")
            continue

        
        try:
           
            a = get_valid_number("Enter the first number: ")
            b = get_valid_number("Enter the second number: ")


            operations = {
                "1": add,
                "2": subtract,
                "3": multiply,
                "4": divide,
            }

            result = operations[choice](a, b)
            
            print(f"\nResult: {result:g}")


        except ValueError as error:
            print(f"Error: {error}")



if __name__ == "__main__":
    main()

