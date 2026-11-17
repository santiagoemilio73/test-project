"""Input parsing and validation helpers."""

from __future__ import annotations

import math


def parse_number(raw: str) -> float:
    """Parse ``raw`` into a finite float.

    Raises:
        ValueError: If the input is empty, not a number, or not finite.
    """
    text = raw.strip()
    if not text:
        raise ValueError("Input cannot be empty.")

    try:
        value = float(text)
    except ValueError:
        raise ValueError(f"{raw!r} is not a valid number.") from None

    if not math.isfinite(value):
        raise ValueError(f"{raw!r} must be a finite number.")

    return value
