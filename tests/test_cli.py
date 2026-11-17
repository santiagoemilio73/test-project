"""Tests for the interactive command-line interface."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from calculator.cli import format_result, run


class FormatResultTests(unittest.TestCase):
    def test_integer_result_has_no_decimal_point(self) -> None:
        self.assertEqual(format_result(42.0), "42")

    def test_decimal_result_is_preserved(self) -> None:
        self.assertEqual(format_result(3.5), "3.5")

    def test_trailing_zeros_are_removed(self) -> None:
        self.assertEqual(format_result(2.500), "2.5")


class RunTests(unittest.TestCase):
    def run_with_inputs(self, *values: str) -> str:
        output = io.StringIO()
        with patch("builtins.input", side_effect=list(values)), redirect_stdout(
            output
        ):
            run()
        return output.getvalue()

    def test_performs_calculation(self) -> None:
        output = self.run_with_inputs("+", "2", "3", "q")
        self.assertIn("Result: 5", output)

    def test_quits_at_operation_prompt(self) -> None:
        output = self.run_with_inputs("q")
        self.assertIn("Goodbye!", output)

    def test_quit_is_case_insensitive(self) -> None:
        output = self.run_with_inputs("QUIT")
        self.assertIn("Goodbye!", output)

    def test_rejects_unsupported_operator(self) -> None:
        output = self.run_with_inputs("%", "q")
        self.assertIn("Error: choose one of +, -, *, /.", output)

    def test_rejects_invalid_number(self) -> None:
        output = self.run_with_inputs("+", "abc", "q")
        self.assertIn("is not a valid number.", output)

    def test_reports_division_by_zero(self) -> None:
        output = self.run_with_inputs("/", "1", "0", "q")
        self.assertIn("Error: Cannot divide by zero.", output)

    def test_handles_end_of_input(self) -> None:
        output = io.StringIO()
        with patch("builtins.input", side_effect=EOFError), redirect_stdout(output):
            run()
        self.assertIn("Goodbye!", output.getvalue())

    def test_handles_keyboard_interrupt(self) -> None:
        output = io.StringIO()
        with patch(
            "builtins.input", side_effect=KeyboardInterrupt
        ), redirect_stdout(output):
            run()
        self.assertIn("Goodbye!", output.getvalue())


if __name__ == "__main__":
    unittest.main()
