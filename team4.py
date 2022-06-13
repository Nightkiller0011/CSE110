"""
File: team4.py
Author: Joshua Ellis

Purpose: Calculate grades.

Above and Beyond completed.
"""
import math

grade = int(input(f"\nWhat is your grade percent? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else: 
    letter = "F"

sign = grade % 10

if sign >= 7:
    signis = "+"
elif sign >= 3:
    signis = ""
else:
    signis = "-"

if grade >= 93 or grade <= 59:
    signis = ""

print(f"Your letter grade is {letter}{signis}.\n")

if letter == "A" or letter == "B" or letter == "C":
    print(f"Congratulations! You passed the class!\n")
else: 
    print(f"Looks like you will have to re-take the class next time... Stay focused and you'll get it next time!\n")
