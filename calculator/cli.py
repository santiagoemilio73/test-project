"""Interactive command-line interface for the calculator."""

from __future__ import annotations

from calculator.operations import OPERATIONS, calculate
from calculator.validation import parse_number

QUIT_COMMANDS = {"q", "quit"}


def format_result(value: float) -> str:
    """Format a result without trailing zeros where possible."""
    return f"{value:g}"


def run() -> None:
    """Run the interactive calculator until the user quits."""
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    print("Type 'q' at the operation prompt to quit.")

    while True:
        try:
            operator = input("Operation: ").strip()
            if operator.lower() in QUIT_COMMANDS:
                print("Goodbye!")
                break
            if operator not in OPERATIONS:
                print("Error: choose one of +, -, *, /.")
                continue

            left = parse_number(input("First number: "))
            right = parse_number(input("Second number: "))
            result = calculate(operator, left, right)
        except (ValueError, ZeroDivisionError) as exc:
            print(f"Error: {exc}")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        else:
            print(f"Result: {format_result(result)}")


def main() -> None:
    """Entry point for the calculator CLI."""
    run()
