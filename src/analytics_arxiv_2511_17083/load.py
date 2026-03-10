from pathlib import Path

from sympy import sympify, Basic


def load_file(file: Path | str) -> Basic:
    with open(file) as f:
        return sympify(f.read())
