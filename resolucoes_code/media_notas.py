"""Grade average helpers."""

from typing import Iterable


def grade_average(grades: Iterable[float]) -> float:
    """Return the arithmetic mean for the provided *grades*.

    Raises a ValueError when no grades are passed.
    """
    grades_list = list(grades)
    if not grades_list:
        raise ValueError("At least one grade is required to compute the average.")
    return sum(grades_list) / len(grades_list)


def prompt_and_average() -> float:
    """Read three grades from the console and print the average."""
    entries: list[float] = []
    for index in range(1, 4):
        raw_grade = input(f"Digite a nota {index}: ")
        try:
            entries.append(float(raw_grade))
        except ValueError as exc:
            raise ValueError("As notas devem ser numericas.") from exc
    result = grade_average(entries)
    print(f"Media: {result:.2f}")
    return result


if __name__ == "__main__":
    prompt_and_average()
