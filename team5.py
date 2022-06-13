"""
File: team5.py
Author: Joshua Ellis

Purpose: Prompt Riders for age and height.

Above and Beyond completed.
"""
import math

single_age_limit = 18
single_height_limit = 62
height_limit = 36

age1 = int(input(f"\n\n\n\nWhat is the age of the first rider? "))
height1 = int(input(f"What is the height of the first rider? "))
age2 = 0
height2 = 0
age3 = 0
height3 = 0
second = input(f"Is there a second rider? ")
if (age1 >= 18 and height1 >= 62) and (second == "no"or second == "No"):
    print(f"Welcome to the ride. Please be safe and have fun!\n") 
# elif (second == "yes" or second == "Yes"):
elif second.lower() == "yes":
    age2 = int(input(f"What is the age of the second rider? "))
    height2 = int(input(f"What is the height of the second rider? "))
else:
    print(f"Sorry, You may not ride. \n")
if age1 >= age2:
    age3 = age1
else: 
    age3 = age2
if height1 >= height2:
    height3 = height1
else: 
    height3 = height2

if (age3 >= 18 and height3 >= 62) and (height1 >= 36 and height2 >= 36):
    print(f"Welcome to the ride. Please be safe and have fun!\n")
else:
    print(f"Sorry, you may not ride.\n")
