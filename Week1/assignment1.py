"""
File: assignment1.py
Author: Joshua Ellis

Purpose: Ask and answer questions.

My above and Beyond was using different methods to print the answer to the screen,
    as well as consolidating things to make it simpler to understand.
"""

questionColor = 'What is your favorite color? '
respondColor = 'Your favorite color is '
questionFirstName = 'What is your first name? '
questionLastName = 'What is your last name? '
respondName = 'Your name is '

color = input(questionColor)
print(respondColor + color + "! Congratulations!")

fName = input(questionFirstName)
lName = input(questionLastName)

print(f"{respondName}{fName.capitalize()} {lName.capitalize()}! That\'s a good name!")
