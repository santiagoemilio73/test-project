"""Arithmetic operations used by the calculator."""

from __future__ import annotations

from collections.abc import Callable


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def subtract(left: float, right: float) -> float:
    """Return the difference of two numbers."""
    return left - right


def multiply(left: float, right: float) -> float:
    """Return the product of two numbers."""
    return left * right


def divide(left: float, right: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If ``right`` is zero.
    """
    if right == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return left / right


OPERATIONS: dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(operator: str, left: float, right: float) -> float:
    """Apply ``operator`` to ``left`` and ``right``.

    Raises:
        ValueError: If the operator is not supported.
        ZeroDivisionError: If dividing by zero.
    """
    try:
        operation = OPERATIONS[operator]
    except KeyError:
        raise ValueError(f"Unsupported operation: {operator!r}") from None
    return operation(left, right)
