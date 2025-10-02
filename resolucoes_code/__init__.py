"""Utility package containing the algorithm exercises."""

from .concat_dados import concatenate, prompt_and_concat
from .media_notas import grade_average, prompt_and_average
from .ope_mat import prompt_and_solve, simple_operation
from .palindromo import is_palindrome, prompt_and_check
from .paridade import describe_parity, is_even, prompt_and_describe
from .repet_txt import prompt_and_repeat, repeat_text

__all__ = [
    "concatenate",
    "describe_parity",
    "grade_average",
    "is_even",
    "is_palindrome",
    "prompt_and_average",
    "prompt_and_check",
    "prompt_and_concat",
    "prompt_and_describe",
    "prompt_and_repeat",
    "prompt_and_solve",
    "repeat_text",
    "simple_operation",
]
