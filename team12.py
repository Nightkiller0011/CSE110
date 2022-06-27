"""
File: team12.py
Author: Joshua Ellis

Purpose: compute values inside functions.

Above and Beyond completed.
"""
import math


def area_square(length):
    area = area_rectangle(length,length)
    return area
def area_rectangle(length, width):
    area = length * width
    return area
def area_circle(radius):
    area = math.pi*(radius**2)
    return area
def compute_area(shape, number, number2=0):
    if shape.lower() == "square":
        area = area_square(number)
    elif shape.lower() == "circle":
        area = area_circle(number)
    elif shape.lower() == "rectangle":
        area = area_rectangle(number,number2)
    return area



def main():
    again = 'y'
    while again == 'y':
        area = 0
        print(f"\nPossible  shapes- Square, Rectangle, Circle.")
        shape = input(f"What shape would you like to use? ")
        if shape.lower() == "square":
            measure1 = float(input(f"What is the length of the side of the square? "))
            area = compute_area(shape, measure1)
            print(f"\nThe area of the {shape} is {area}.")
        elif shape.lower() == "rectangle":
            measure1 = float(input(f"What is the length of the rectangle? "))
            measure2 = float(input(f"What is the width of the rectangle? "))
            area = compute_area(shape, measure1,measure2)
            print(f"\nThe area of the {shape} is {area}.")
        elif shape.lower() == "circle":
            measure1 = float(input(f"What is the radius of the circle? "))
            area = compute_area(shape, measure1)
            print(f"\nThe area of the {shape} is {area}.")
        else:
            print(f"That was not an option, please choose again.")
        again = input(f"\nWould you like to try again?(y/n) ")
    return

main()






