"""
File: team2.py
Author: Joshua Ellis

Purpose: Calculate the area of shapes.

Above and Beyond completed.
"""
import math
def ask(question):
    answer = int(input(question))
    return answer
lengthS = ask(f"\nWhat is the length of a side of the square? ")
print(f"The area of the square is: {lengthS**2}")
lengthR = ask(f"What is the length of the rectangle? ")
widthR = ask(f"What is the width of the rectangle? ")
print(f"The area of the rectangle is: {lengthR*widthR}")
circleR = ask(f"What is the radius of the circle? ")
print(f"The area of the circle is: {math.pi*(circleR**2)}\n")

lengthD = ask(f"What about a length for all 3? ")
print(f"Square: {lengthD**2}\nCircle: {math.pi*(lengthD**2)}\nCube: {lengthD**3}\nSphere: {(4/3)*math.pi*(lengthD**3)}\n")

lengthScm = ask(f"\nWhat is the length of a side of the square in centimeters? ")
print(f"The area of the square is: {lengthScm**2} cm^2\nThe area of the square is: {(lengthScm**2)/1000} m^2")
lengthRcm = ask(f"What is the length of the rectangle in centimeters? ")
widthRcm = ask(f"What is the width of the rectangle in centimeters? ")
print(f"The area of the rectangle is: {lengthRcm*widthRcm} cm^2\nThe area of the rectangle is: {(lengthRcm*widthRcm)/1000} m^2")
circleRcm = ask(f"What is the radius of the circle in centimeters? ")
print(f"The area of the circle is: {math.pi*(circleRcm**2)} cm^2\nThe area of the circle is: {(math.pi*(circleRcm**2))/1000} m^2")




