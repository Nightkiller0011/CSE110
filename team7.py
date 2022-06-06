"""
File: team7.py
Author: Joshua Ellis

Purpose: Higher/Lower game.

Above and Beyond completed.
"""
word = "commitment"
favorite = input(f"What is your favorite letter? ")
for letter in word:
    if letter == favorite:
        print(f'{letter.upper()}', end="")
    else:
        print(f'{letter.lower()}', end="")
print()
for letter in word:
    if letter == favorite.lower():
        print(f'_', end="")
    else:
        print(f'{letter.lower()}', end="")
print()

again = 'y'
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
while again == 'y':
    num = int(input("Please enter a number: "))
    for i, letter in enumerate(quote):
        if i % num == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    print()
    again = input(f"Try again?(y/n) ")
print(f"Goodbye!")