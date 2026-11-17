
# VEYRA Smart Calculator

A modular Python command-line calculator developed by **VEYRA Digital Studio**.

## Overview

VEYRA Smart Calculator is a Python application designed to perform basic arithmetic operations through an interactive, menu-driven interface.

The project demonstrates fundamental software engineering principles, including separation of concerns, reusable functions, input validation, exception handling, modular architecture, and automated unit testing.

This application is part of the VEYRA Digital Studio software development portfolio.

## Features

- **Four arithmetic operations:** Addition, subtraction, multiplication, and division.
- **Interactive command-line interface:** Menu-driven navigation for selecting operations.
- **Input validation:** Rejects invalid and non-finite numerical inputs.
- **Error handling:** Prevents division by zero and handles invalid menu selections.
- **Modular architecture:** Separates application logic, calculations, and input validation.
- **Automated unit testing:** Uses Python's built-in `unittest` framework.
- **Readable results:** Displays numerical results without unnecessary trailing zeros.

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core application development |
| Visual Studio Code | Development environment |
| unittest | Automated unit testing |
| Git | Version control |
| GitHub | Source code hosting and portfolio |
| Markdown | Project documentation |

## Project Structure

```text
VEYRA-Smart-Calculator/
├── main.py
├── calculator.py
├── validation.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── .gitignore
└── README.md
```

### File Descriptions

**main.py**

The main application entry point. Provides the interactive menu, processes user selections, and displays calculation results.

**calculator.py**

Contains reusable arithmetic functions for addition, subtraction, multiplication, and division.

**validation.py**

Handles numerical input validation and prevents invalid or non-finite values from being processed.

**tests/test_calculator.py**

Contains automated unit tests for verifying arithmetic operations, error handling, negative numbers, and decimal calculations.

**.gitignore**

Excludes unnecessary development files, Python cache directories, virtual environments, and local configuration files from version control.

## Installation

### Prerequisites

- Python 3.10 or later
- Git (optional, for cloning the repository)
- Visual Studio Code (optional)

No third-party Python packages are required.

### Clone the Repository

```bash
git clone https://github.com/Kai-Deux/VEYRA-Smart-Calculator.git
```

### Open the Project

```bash
cd VEYRA-Smart-Calculator
```

## Usage

Run the application using Python:

```bash
python main.py
```

Alternatively, open `main.py` in Visual Studio Code and select **Run Python File**.

Follow the interactive menu to:

1. Select an arithmetic operation.
2. Enter the first number.
3. Enter the second number.
4. View the calculated result.
5. Continue calculating or exit the application.

The application validates numerical input and handles division-by-zero errors.

## Automated Testing

VEYRA Smart Calculator includes automated unit tests built with Python's `unittest` framework.

### Test Coverage

The test suite covers:

- Addition, subtraction, multiplication, and division
- Division-by-zero error handling
- Negative number calculations
- Decimal precision
- Multiple arithmetic test cases using `subTest()`

### Running the Tests

From the project's root directory, run:

```bash
python -m unittest discover -s tests -v
```

Alternatively, execute the tests through the **Testing** panel in Visual Studio Code.

The tests verify that the calculator's arithmetic functions produce the expected results.

## Software Engineering Practices

This project demonstrates:

- Modular programming
- Separation of concerns
- Reusable functions
- Input validation
- Exception handling
- Automated unit testing
- Git version control
- Technical documentation

## Future Enhancements

Potential improvements include:

- Calculation history
- Additional mathematical operations
- Graphical user interface (GUI)
- Persistent storage of calculations
- Continuous integration using GitHub Actions

These enhancements are planned possibilities and are not part of the current release.

## Developer

**VEYRA Digital Studio**

Software Development | Python | Automation | IT Solutions

GitHub: https://github.com/Kai-Deux

## Version

**1.0.0**

Initial release featuring modular arithmetic operations, interactive input handling, validation, and automated unit testing.
