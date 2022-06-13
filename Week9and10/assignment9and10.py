"""
File: assignment9and10.py
Author: Joshua Ellis

Purpose: Create a menu with options and allow the user to cycle through them.

# Above and Beyond completed.
"""

def main():
    shopping_cart = []
    item = None
    shopping_price = []
    price = None
    cycle = 'y'
    while cycle == 'y':
        option = 'y'
        print(f"cycle_active")
        while option != '5':
            # print(f"menu_active")
            print(f"\nMenu Options: \n1. - Add New Item\n2. - Display Contents of Cart\n3. - Remove Item from Cart\n4. - Compute Total of Cart\n5. - Quit\n")
            option = input("You choose: ")
            if option == '1':
                price = -1
                print()
                item = input(f"What item would you like to add? ")
                
                while price < 0:
                    price = float(input(f"What is the price of {item}? $"))
                
                
                shopping_cart.append(item)
                shopping_price.append(price)
                print(f"Item - {item} : ${price} - was added to cart.")
            elif option == '2':
                print()
                for i, items in enumerate(shopping_cart):
                    print(f"{i+1}. {shopping_cart[i-1]}: ${shopping_price[i-1]:.2f}")
            elif option == '3':
                remover = input(f"What is the item called you would like to remove? ")
                x = shopping_cart.index(remover)
                shopping_cart.pop(x)
                shopping_price.pop(x)
            elif option == '4':
                total = 0
                for i, prices in enumerate(shopping_price):
                    total = total + prices
                print(f"The total Price is {total:.2f}.")
            elif option == '5':
                pass
            else:
                print(f"That is not a viable option. Please Try again.")
            
        cycle = input(f"\nWould you like to shop again?(y/n) ")


main()