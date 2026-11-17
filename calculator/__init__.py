"""A simple, dependency-free command-line calculator."""

from calculator.operations import (
    OPERATIONS,
    add,
    calculate,
    divide,
    multiply,
    subtract,
)
from calculator.validation import parse_number

__all__ = [
    "OPERATIONS",
    "add",
    "calculate",
    "divide",
    "multiply",
    "parse_number",
    "subtract",
]
