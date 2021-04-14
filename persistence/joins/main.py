
import database

def menu():
    print("Select one of the following options:")
    print("[1] Display stock levels")
    print("[2] Display suppliers")
    print("[3] Display supplier locations")
    print("[4] Display missing suppliers")


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
    elif selected_option == 4:
        database.display_products_missing_suppliers()
    else:
        print("Invalid selection... try again")
        run()


if __name__ == "__main__":
    run()
