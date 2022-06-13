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
        update_option = None
        print(f"\nEnter the names and balances of bank accounts (type: quit when done)")
        while name != "quit":
            if update_option == "y":
                name = "quit"
            else:
                name = input(f"What is the name of the account? ")
            if name == "quit":
                print(f"\nAccount Information:\n")
                for i, items in enumerate(account_name):
                    print(f"{items} - ${account_balance[i]}")
                print(f"\nTotal: ${sum:.2f}\nAverage: ${average:.2f}\nHighest: {highest_account} - ${highest:.2f}")
                print()
                update_option = input(f"Would you like to update an account?(y/n) ")
                if update_option == "y":
                    name = input(f"What is the name of the account that you want to Update? ")
                    balance = int(input(f"What is the new balance is in the account? "))
                    i_number = account_name.index(name)
                    sum -= account_balance[i_number] 
                    sum += balance
                    account_balance.pop(i_number)
                    account_balance.insert(i_number, balance)
                    if highest < balance:
                        highest = balance
                        highest_account = name
                else:
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



        test_again = input(f"\nWould you like to repeat the code again?(y/n) ")

main()