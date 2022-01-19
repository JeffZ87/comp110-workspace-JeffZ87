"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730480180"

for y in range(20):
    WORD: str = input("Enter a 5-character word: ")
    match_count: int = 0
    
    if len(WORD) != 5 or not(WORD.isalpha()):
        print("Error: Word must contain 5 characters")
    else: 
        CHAR: str = input("Enter a single character ")
        if len(CHAR) != 1 or not(CHAR.isalpha()):
            print("Error: Character must be a single character.")
        else:
            print("Searching for " + CHAR + " in " + WORD)
            for x in range(len(WORD)):
                if CHAR == WORD[x]:
                    print(CHAR + " found at index " + str(x))
                    match_count += 1
            if(match_count > 0):
                print(str(match_count) + " instances of " + CHAR + " found in " + WORD)
            else:
                print("No instances of " + CHAR + " found in " + WORD)