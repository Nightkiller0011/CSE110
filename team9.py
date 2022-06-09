"""
File: team9.py
Author: Joshua Ellis

Purpose: Create a program to store and calculate prices with matching accounts.

Above and Beyond completed.
"""


def main():
    test_again = "y"
    while test_again.lower() == "y":
        account_name = []
        name = None
        account_balance = []
        balance = None
        sum = 0
        average = 0
        x = 0
        highest_account = None
        highest = 0
        print(f"\nEnter the names and balances of bank accounts (type: quit when done)")
        while name != "quit":
            name = input(f"What is the name of the account? ")
            if name == "quit":
                print(f"\nAccount Information:\n")
                for i, items in enumerate(account_name):
                    print(f"{items} - ${account_balance[i]}")
                print(f"\nTotal: ${sum:.2f}\nAverage: ${average:.2f}\nHighest: {highest_account} - ${highest:.2f}")

                

            else:
                balance = int(input(f"How much money is in the account? "))
                x += 1
                account_name.append(name)
                account_balance.append(balance)
                sum += balance
                if highest < balance:
                    highest = balance
                    highest_account = name
            average = sum/x



        test_again = input(f"Would you like to test the code again?(y/n) ")

main()