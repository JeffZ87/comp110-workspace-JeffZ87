"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730480180"


for x in range(20):
    WORD: str = input("Enter a 5-character word: ")

    if len(WORD) != 5 or not(WORD.isalpha()):
        print("Error: Word must contain 5 characters")
        exit()

    CHAR: str = input("Enter a single character ")

    if len(CHAR) != 1 or not(CHAR.isalpha()):
        print("Error: Character must be a single character.")
        exit()

    match_count: int = 0
    print("Searching for " + CHAR + " in " + WORD)

    if WORD[0] == CHAR:
        print(CHAR + " found at index " + str(0))
        match_count += 1
    if WORD[1] == CHAR:
        print(CHAR + " found at index " + str(1))
        match_count += 1
    if WORD[2] == CHAR:
        print(CHAR + " found at index " + str(2))
        match_count += 1
    if WORD[3] == CHAR:
        print(CHAR + " found at index " + str(3))
        match_count += 1
    if WORD[4] == CHAR:
        print(CHAR + " found at index " + str(4))
        match_count += 1

    if match_count > 0:
        if match_count == 1:
            print(str(match_count) + " instance of " + CHAR + " found in " + WORD)
        else:
            print(str(match_count) + " instances of " + CHAR + " found in " + WORD)
    else:
        print("No instances of " + CHAR + " found in " + WORD)