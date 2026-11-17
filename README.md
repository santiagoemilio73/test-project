# test-project

A simple, dependency-free command-line calculator written in Python. It supports
addition, subtraction, multiplication, and division with input validation and
clear error handling.

## Features

- Four arithmetic operations: `+`, `-`, `*`, `/`
- Validates numeric input (rejects empty, non-numeric, and non-finite values)
- Handles division by zero and unsupported operations gracefully
- Interactive prompt; type `q` to quit
- Test suite built entirely on the standard library

## Requirements

- Python 3.10 or newer (developed and tested with Python 3.14)
- No third-party dependencies

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd test-project
   ```

2. (Optional) Confirm Python is available:

   ```bash
   python3 --version
   ```

No installation step is required.

## Usage

From the project root:

```bash
python3 main.py
```

Example session:

```
Simple Calculator
Operations: +  -  *  /
Type 'q' at the operation prompt to quit.
Operation: *
First number: 6
Second number: 7
Result: 42
Operation: /
First number: 10
Second number: 0
Error: Cannot divide by zero.
Operation: q
Goodbye!
```

## Project structure

```
test-project/
├── calculator/
│   ├── __init__.py      # Package exports
│   ├── cli.py           # Interactive command-line interface
│   ├── operations.py    # Arithmetic functions and dispatch
│   └── validation.py    # Numeric input parsing and validation
├── tests/
│   ├── __init__.py
│   ├── test_operations.py
│   └── test_validation.py
├── main.py              # Entry point
└── README.md
```

## Testing

Run the full test suite from the project root:

```bash
python3 -m unittest discover -v
```

You can also target a single module:

```bash
python3 -m unittest tests.test_operations -v
```

## License

No license has been specified for this project.
