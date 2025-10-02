"""Basic arithmetic operations."""

from collections.abc import Callable

Operation = Callable[[float, float], float]


def simple_operation(left: float, right: float, operator: str) -> float:
    """Apply one of the supported operators to *left* and *right*.

    The supported operators are +, -, *, /.
    """
    operations: dict[str, Operation] = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": _safe_division,
    }
    if operator not in operations:
        raise ValueError("Unsupported operator. Use one of +, -, *, /.")
    return operations[operator](left, right)


def _safe_division(left: float, right: float) -> float:
    if right == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return left / right


def prompt_and_solve() -> float:
    """Interactive arithmetic helper."""
    first = float(input("Digite o primeiro numero: "))
    second = float(input("Digite o segundo numero: "))
    operator = input("Escolha a operacao (+, -, *, /): ")
    result = simple_operation(first, second, operator)
    print(f"Resultado: {result}")
    return result


if __name__ == "__main__":
    prompt_and_solve()
