"""Tests for arithmetic operations."""

import unittest

from calculator.operations import (
    OPERATIONS,
    add,
    calculate,
    divide,
    multiply,
    subtract,
)


class ArithmeticTests(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1.5, 0.5), -1.0)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0.25, 1), -0.75)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(-2, 3.5), -7.0)

    def test_divide(self) -> None:
        self.assertEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(1, 3), 1 / 3)

    def test_divide_by_zero_raises(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)


class CalculateDispatchTests(unittest.TestCase):
    def test_all_operators_dispatch(self) -> None:
        self.assertEqual(calculate("+", 2, 3), 5)
        self.assertEqual(calculate("-", 2, 3), -1)
        self.assertEqual(calculate("*", 2, 3), 6)
        self.assertEqual(calculate("/", 6, 3), 2)

    def test_operation_table_matches(self) -> None:
        self.assertEqual(set(OPERATIONS), {"+", "-", "*", "/"})

    def test_unsupported_operator_raises(self) -> None:
        with self.assertRaises(ValueError):
            calculate("%", 1, 2)

    def test_division_by_zero_propagates(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            calculate("/", 1, 0)


if __name__ == "__main__":
    unittest.main()
