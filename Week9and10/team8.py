"""
File: team8.py
Author: Joshua Ellis

Purpose: creating a list and finding the average.

Above and Beyond completed.
"""
play = 'y'
print(f"Welcome.")
while play == 'y':
    print(f"\nEnter a list of numbers, type 0 when finished.")

    numbers = []
    number = None
    sum = 0
    count = 0
    average = 0
    lnumber = 0
    spnumber = 100
    while number != 0:
        number = int(input(f"Enter Number: "))
        if number != 0:
            sum += number
            count += 1
            average = sum/count
            if number > lnumber:
                lnumber = number
            if number >0 and number< spnumber:
                spnumber = number
        if number != 0:
            numbers.append(number)

    print()
    print(f"The Sum is: {sum}")
    print(f"The average is: {average}")
    print(f"The Largest Number is: {lnumber}")
    print(f"The Smallest Positive Number is: {spnumber}")
    print(f"The sorted list is: ")
    sorted = sorted(numbers)
    for each in sorted:
        print(f"{each}")

    play = input(f"\nPlay again?(y/n) ")
print(f"Thanks for playing!")