"""Command line interface to explore the exercises."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from . import (
    prompt_and_average,
    prompt_and_check,
    prompt_and_concat,
    prompt_and_describe,
    prompt_and_repeat,
    prompt_and_solve,
)


@dataclass
class MenuItem:
    label: str
    action: Callable[[], object]


def build_menu() -> dict[str, MenuItem]:
    return {
        "1": MenuItem("Concatenar dados", prompt_and_concat),
        "2": MenuItem("Repetir texto", prompt_and_repeat),
        "3": MenuItem("Operacoes matematicas", prompt_and_solve),
        "4": MenuItem("Verificar paridade", prompt_and_describe),
        "5": MenuItem("Calcular media de notas", prompt_and_average),
        "6": MenuItem("Verificar palindromo", prompt_and_check),
        "0": MenuItem("Sair", lambda: None),
    }


def main() -> None:
    menu = build_menu()
    while True:
        print("\nEscolha uma opcao:")
        for key, item in sorted(menu.items()):
            print(f" {key} - {item.label}")
        choice = input("Digite a opcao desejada: ")
        if choice == "0":
            print("Saindo...")
            return
        option = menu.get(choice)
        if option is None:
            print("Opcao invalida. Tente novamente.")
            continue
        try:
            option.action()
        except Exception as exc:  # noqa: BLE001
            print(f"Ocorreu um erro: {exc}")


if __name__ == "__main__":
    main()
