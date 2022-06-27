"""
File: assignment13.py
Author: Joshua Ellis

Purpose: This program calculates wind chill.

# Above and Beyond completed.
"""
import math

def calculate(V,T,degree):
    if degree.upper() == 'C':
        T = (T * (9/5)) + 32
    elif degree.upper() == 'K':
        T = T - 273.15
    answer = 35.74 + (0.6215 * T) - (35.75*(V**.16)) + (0.4275*T*(V**.16))
    return answer



def main():
    wind_list = [5,10,15,20,25,30,35,40,45,50,55,60]
    temp = float(input(f"\nWhat is the temperature? "))
    degree = input(f"Fahrenheit or Celsius (F/C/K)? ")
    for wind in wind_list:
        chill = calculate(wind, temp, degree)
        print(f"At temperature {temp:.0f}{degree}, and  speed {wind} mph, the windchill is: {chill:.2f}F")

main()