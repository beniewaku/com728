# Module main.py. This module contains the following functions:
#
# A function named menu that displays a menu of options as shown below and returns an integer corresponding to the
# option selected by the user:


import database

def menu():
    print("Select one of the following options:")
    print("[1] Display stock levels")
    print("[2] Display suppliers")


    selected_option = int(input("Your selection choice: "))
    return selected_option

def run():
    selected_option = menu()
    if selected_option == 1:
        database.display_products_with_stock_levels()
    elif selected_option == 2:
        database.display_product_supplier()
    else:
        print("Invalid selection... try again")
        run()


if __name__ == "__main__":
    run()
