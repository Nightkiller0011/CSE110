"""
File: team6.py
Author: Joshua Ellis

Purpose: Higher or Lower Game.

Above and Beyond completed.
"""
import random
playagain = 'yes'
while playagain.lower() == "yes":
    range = int(input(f"A number between 0 and :"))
    magic_number = random.randint(1, range)
    go_again = 1
    guesses = 0
    while go_again == 1:
        guess = int(input(f"What is your guess? "))
        if guess > magic_number:
            print(f"Lower")
            guesses = guesses + 1
        elif guess == magic_number:
            print(f"You guessed it! You guessed {guesses} times!")
            go_again = 0

        else: 
            print(f"Higher")
            guesses = guesses + 1
    playagain = input(f"Would you like to play again? ")
