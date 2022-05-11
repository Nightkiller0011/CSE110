"""
File: assignment3and4.py
Author: Joshua Ellis

Purpose: Find the total and prices associated with a families night out.

# Above and Beyond completed.
"""
import math
def askf(question):
    answer = float(input(question))
    return answer
def aski(question):
    answer = int(input(question))
    return answer
childPrice = askf("\nWhat is the price of a child\'s meal? ")
adultPrice = askf("What is the price of an adult\'s meal? ")
childCount = aski("How many children are there? ")
adultCount = aski("How many adults are there? ")
taxRate = aski("What is the sales tax rate? ")
taxMult = (taxRate/100)
subtotal = (childCount*childPrice)+(adultCount*adultPrice)
tax = subtotal*taxMult
total = subtotal+tax
print(f"Subtotal: ${subtotal:.2f}\nSales Tax: ${tax:.2f}\nTotal: ${total:.2f}\n")
payment = aski("\nWhat is the payment amount? ")
change = payment - total
print(f"Change: ${change:.2f}")
