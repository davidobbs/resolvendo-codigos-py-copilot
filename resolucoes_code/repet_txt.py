"""Text repetition helpers."""


def repeat_text(text: str, times: int, separator: str | None = None) -> str:
    """Repeat *text* the specified number of *times*.

    When a separator is given the copies are joined using it. A ValueError is
    raised for negative repetition counts.
    """
    if times < 0:
        raise ValueError("times must be zero or greater")
    if times == 0:
        return ""
    if separator is not None:
        return separator.join(text for _ in range(times))
    return text * times


def prompt_and_repeat() -> str:
    """Interactive prompt that repeats text according to user input."""
    message = input("Digite o texto que deseja repetir: ")
    raw_times = input("Digite o numero de repeticoes: ")
    try:
        times = int(raw_times)
    except ValueError as exc:
        raise ValueError("O numero de repeticoes deve ser inteiro.") from exc
    result = repeat_text(message, times, separator=" ")
    print(f"Resultado: {result}")
    return result


if __name__ == "__main__":
    prompt_and_repeat()
