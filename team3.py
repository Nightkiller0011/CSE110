"""
File: team3.py
Author: Joshua Ellis

Purpose: Determine how fast an object will fall.

Above and Beyond completed.
"""

import math



print(f"Welcome to the velocity calculator. Please enter the following:\n")
# mass
m = int(input(f"Mass (in kg): "))
# gravity
g = float(input(f"Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
# time
t = int(input(f"Time (in seconds): "))
# density of fluid
p = float(input(f"Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
# cross sectional area
A = float(input(f"Cross sectional area (in m^2): "))
# drag constant
C = float(input(f"Crag constant (0.5 for sphere, 1.1 for cylinder): "))

c = (1 / 2) * p * A * C
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t))

print(f"\nThe inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {v:.3f} m/s")
