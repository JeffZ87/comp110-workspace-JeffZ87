"""Examples of importing Python."""

from lessons import helpers
# from lessons import helpers as hp
from lessons.helpers import powerful
print("end of import")


def main() -> None:
    """Entrypoint of program."""
    print(powerful(2, 4))
    print(helpers.THE_ANSWER)


if __name__ == "__main__":
    main()