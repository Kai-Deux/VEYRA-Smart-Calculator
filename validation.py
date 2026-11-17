
# VEYRA Digital Studio
# Module: Input Validation

import math


def get_valid_number(prompt: str) -> float:
    """Prompt until the user enters a finite number."""

    while True:
        user_input = input(prompt).strip()

        try:
            number = float(user_input)

            if not math.isfinite(number):
                print("Error: Enter a finite number.")
                continue

            return number

        except ValueError:
            print("Invalid input. Please enter a number.")
