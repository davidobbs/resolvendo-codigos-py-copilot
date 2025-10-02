"""Parity helpers."""


def is_even(value: int) -> bool:
    """Return True when *value* is even."""
    return value % 2 == 0


def describe_parity(value: int) -> str:
    """Return a human friendly description of the parity of *value*."""
    if is_even(value):
        return f"{value} e um numero par"
    return f"{value} e um numero impar"


def prompt_and_describe() -> str:
    """Interactive helper that prints the parity of a provided integer."""
    raw_value = input("Digite um numero inteiro: ")
    try:
        number = int(raw_value)
    except ValueError as exc:
        raise ValueError("A entrada deve ser um numero inteiro.") from exc
    message = describe_parity(number)
    print(message)
    return message


if __name__ == "__main__":
    prompt_and_describe()
