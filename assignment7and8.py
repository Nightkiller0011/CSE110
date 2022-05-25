"""
File: assignment7and8.py
Author: Joshua Ellis

Purpose: Create and Guess a secret word.

# Above and Beyond completed.
"""
import random
playagain = 'yes'
while playagain.lower() == "yes":
    print(f"\n  /------------\\ \nGenerating new word.\n  \\------------/ \n")
    go_again = 1
    guesses = 0
    hint = ""
    word = ""
    print(f"Your hint is: {hint}\n")
    while go_again == 1:
        guess = input(f"What is your guess? ")
        if guess.lower() == word:
            go_again = 0
            print(f"Good job! you guessed it! ")
        else:
            print(f"Your hint is: {hint}\n")
        go_again = int(input(f"Test Go_Again: "))
    playagain = input(f"Would you like to play again? ")
