"""Tests for input parsing and validation."""

import unittest

from calculator.validation import parse_number


class ParseNumberTests(unittest.TestCase):
    def test_integers(self) -> None:
        self.assertEqual(parse_number("42"), 42.0)
        self.assertEqual(parse_number("-7"), -7.0)

    def test_decimals_and_scientific_notation(self) -> None:
        self.assertEqual(parse_number("3.14"), 3.14)
        self.assertEqual(parse_number("1e3"), 1000.0)
        self.assertEqual(parse_number("-2.5E-2"), -0.025)

    def test_whitespace_is_stripped(self) -> None:
        self.assertEqual(parse_number("  8  "), 8.0)

    def test_empty_input_raises(self) -> None:
        with self.assertRaises(ValueError):
            parse_number("")
        with self.assertRaises(ValueError):
            parse_number("   ")

    def test_non_numeric_input_raises(self) -> None:
        for raw in ("abc", "12abc", "1,5", "--2"):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_number(raw)

    def test_non_finite_input_raises(self) -> None:
        for raw in ("nan", "inf", "-inf", "Infinity"):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_number(raw)


if __name__ == "__main__":
    unittest.main()
