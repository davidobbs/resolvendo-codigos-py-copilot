"""Automated checks for the algorithm helpers."""

import pytest

from resolucoes_code import (
    concatenate,
    grade_average,
    is_even,
    is_palindrome,
    repeat_text,
    simple_operation,
)


def test_concatenate_with_separator() -> None:
    assert concatenate("Data", "Science", " ") == "Data Science"


def test_repeat_text_without_separator() -> None:
    assert repeat_text("ab", 3) == "ababab"


def test_repeat_text_with_separator() -> None:
    assert repeat_text("xy", 3, separator="-") == "xy-xy-xy"


def test_repeat_text_negative_times() -> None:
    with pytest.raises(ValueError):
        repeat_text("a", -1)


def test_simple_operation_division() -> None:
    assert simple_operation(10, 2, "/") == 5


def test_simple_operation_unsupported_operator() -> None:
    with pytest.raises(ValueError):
        simple_operation(1, 2, "%")


def test_is_even() -> None:
    assert is_even(42)
    assert not is_even(17)


def test_grade_average() -> None:
    assert grade_average([5, 7, 9]) == pytest.approx(7.0)


def test_grade_average_without_grades() -> None:
    with pytest.raises(ValueError):
        grade_average([])


def test_palindrome_normalization() -> None:
    assert is_palindrome("Socorram-me subi no onibus em Marrocos")

