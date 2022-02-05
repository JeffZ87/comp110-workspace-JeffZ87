"""An example of conditiona (if=else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5 what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have wonderful day!!!")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("you guessed to high!")
    else:
        print("You guessed too low!")

print("Game over.")