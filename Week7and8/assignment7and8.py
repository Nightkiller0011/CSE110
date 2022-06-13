"""
File: assignment7and8.py
Author: Joshua Ellis

Purpose: Create and Guess a secret word.

# Above and Beyond completed.
"""
import random



def hinttest2(word, guess):
    for i, letter1 in enumerate(guess):
        if i > len(word)-1:
            break
        x = word.find(letter1)
        if letter1 == word[i]:
            print(f"{letter1.upper()}", end=" ")
        elif x >=0 :
            print(f"{letter1.lower()}", end=" ")
        else:
            print(f"_", end=" ")
    return



playagain = 'yes'
while playagain.lower() == "yes":
    print(f"\n  /------------\\ \nGenerating new word.\n  \\------------/ \n")
    word_num = random.randint(1, 6)
    go_again = 1
    guesses = 0
    guess = "                                         "
    word = ""
    if word_num == 1:
        word = "bubble"
    elif word_num == 2:
        word = "sandwich"
    elif word_num == 3:
        word = "apples"
    elif word_num == 4:
        word = "crunchy"
    elif word_num == 5:
        word = "montana"
    else:
        word = "supercalifragilisticexpialadocious"
    print(f"Your hint is: ", end="")
    hinttest2(word, guess)
    print()
    while go_again == 1:
        guess = input(f"What is your guess? ")
        if guess.lower() == word:
            go_again = 0
            guesses = guesses + 1
            print(f"Good job! you guessed it! It took you {guesses} Guesses! ")
        else:
            print(f"Your guess was not correct!")
            guesses = guesses + 1
            print(f"Your hint is: ", end="")
            hinttest2(word, guess)
            print()
    playagain = input(f"Would you like to play again? ")
