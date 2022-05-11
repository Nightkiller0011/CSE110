"""
File: assignment5and6.py
Author: Joshua Ellis

Purpose: Text based adventure game.

# Above and Beyond completed.
"""
def gametext(words):
    print(f"\n\n\n{words}\n\n\n")
def display(health, mana, gold):
    print(f"Health:{health:^6d} Mana:{mana:^6d} Gold:{gold:^6d}")

# Set terminal height to 12 lines

health = 10
mana = 6
gold = 0

gametext("\n\nWelcome to the newest Adventure Game!\n\n")
name = input(f"What name will you give your character? ")
display(health,mana,gold)
gametext(f"Welcome to the game {name}!\n\n")



