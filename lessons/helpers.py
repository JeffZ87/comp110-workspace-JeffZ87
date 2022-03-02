"""Defining a module imported elsewhere."""

THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helper.py run as module")


def powerful(x: int, n: float) -> float:
    """Raise x to the power of n"""
    print("powerful is evaluated")
    return x ** n


if __name__ == "__main__":
    main()
else:
    print(f"helper.py was imported: {__name__}")