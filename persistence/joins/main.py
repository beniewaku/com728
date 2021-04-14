
import database

def menu():
    print("Select one of the following options:")
    print("[1] Display stock levels")
    print("[2] Display suppliers")
    print("[3] Display supplier locations")


    selected_option = int(input("Your selection choice: "))
    return selected_option

def run():
    selected_option = menu()
    if selected_option == 1:
        database.display_products_with_stock_levels()
    elif selected_option == 2:
        database.display_product_supplier()
    elif selected_option == 3:
        database.display_product_supplier_locations()
    else:
        print("Invalid selection... try again")
        run()


if __name__ == "__main__":
    run()
