"""ex02_one_shot_wordle: a simplified wordle."""

_author_ = "730480180"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

while len(secret) != len(guess):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

i: int = 0
result_box: str = ""

while i < len(guess):
    if secret[i] == guess[i]:
        result_box += GREEN_BOX
    else:
        j: int = 0
        is_char_in_secret: bool = False

        while j < len(guess):
            if secret[j] == guess[i]:
                result_box += YELLOW_BOX
                is_char_in_secret = True
                j = len(guess)
            else:
                j += 1
        if not is_char_in_secret:
            result_box += WHITE_BOX
    i += 1

print(result_box)

if secret == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")