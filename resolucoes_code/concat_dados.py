"""Concatenation helpers for the challenge exercises."""

from typing import Any


def concatenate(left: Any, right: Any, separator: str = "") -> str:
    """Return the textual concatenation of two values.

    Both inputs are converted to strings before concatenation. The optional
    separator is inserted between the pieces when provided.
    """
    left_text = str(left)
    right_text = str(right)
    if separator:
        return f"{left_text}{separator}{right_text}"
    return f"{left_text}{right_text}"


def prompt_and_concat() -> str:
    """Collect two values from the console, concatenate them, and print."""
    first_value = input("Digite o primeiro dado: ")
    second_value = input("Digite o segundo dado: ")
    result = concatenate(first_value, second_value)
    print(f"Resultado: {result}")
    return result


if __name__ == "__main__":
    prompt_and_concat()
