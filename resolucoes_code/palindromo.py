"""Palindrome verification helpers."""


def is_palindrome(text: str) -> bool:
    """Return True when *text* reads the same backwards and forwards."""
    normalized = _normalize_text(text)
    return normalized == normalized[::-1]


def _normalize_text(text: str) -> str:
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned


def prompt_and_check() -> bool:
    """Interactive palindrome checker."""
    candidate = input("Digite uma palavra ou frase: ")
    result = is_palindrome(candidate)
    if result:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")
    return result


if __name__ == "__main__":
    prompt_and_check()
