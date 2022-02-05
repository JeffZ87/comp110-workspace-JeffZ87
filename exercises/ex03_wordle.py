"""Exercise 03 - building wordle."""

__author__ = "730480180"


def contains_char(word: str, char: str) -> bool:
    """Check if {char} is contained in {word}."""
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Compare {guess} and {secret} then return emojified string."""
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i: int = 0
    result_box: str = ""

    while i < len(guess):
        if secret[i] == guess[i]:
            result_box += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                result_box += YELLOW_BOX
            else:
                result_box += WHITE_BOX
        i += 1
    return result_box


def input_guess(expected_len: int) -> str:
    """Prompt user for input and return input with correct {guess_len} length."""
    guess: str = input(f"Enter a {expected_len} character word: ")
    while expected_len != len(guess):
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    has_won: bool = False
    turn_num: int = 1
    secret: str = "codes"
    while turn_num <= 6 and not has_won:
        print(f"=== Turn {turn_num}/6 ===")
        guess: str = input_guess(len(secret))
        result: str = emojified(guess, secret)
        print(result)
        if secret == guess:
            has_won = True
        else:
            turn_num += 1
    if has_won:
        print(f"You won in {turn_num}/6 turns!")
    else:
        print(" X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()