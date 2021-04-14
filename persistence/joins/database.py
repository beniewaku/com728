# The program consists of several modules as follows:
#
# Module: database.py. This module contains the following functions:
#
# A single function named display_products_with_stock_levels. This function takes no parameters.
# The function should display each product with its stock levels. You should use a natural join to query the database.

import sqlite3

PRODUCT_COLUMN = 0
DESCRIPTION_COLUMN = 1
QUANTITY_COLUMN = 2


def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")

    cursor = db.cursor()

    sql = "SELECT name, description, quantity" \
          " FROM product" \
          " NATURAL JOIN stock"

    cursor.execute(sql)

    record = cursor.fetchall()

    print(f"There are {len(record)}products in the catalogue")
    print(f"The stock level are as follows:")

    for record in record:
        print(f"Product: {record[PRODUCT_COLUMN]}")
        print(f"Description: {record[DESCRIPTION_COLUMN]}")
        print(f"Stock level: {record[QUANTITY_COLUMN]}")
        print()

    db.close()


# Modify your module database so that it contains an additional function named display_product_supplier. This
# function should take no parameters and should display each product with its supplier. You should use a suitable
# inner join to query the database. Modify the function menu in the module main so that it displays an additional
# option: [2] Display suppliers
#
# Modify the function run in the module main so that it calls the function display_product_supplier of the module
# database if the user selects option 2.


def display_product_supplier():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name  " \
          "FROM product " \
          "INNER JOIN supplier ON product.supplier_id = supplier.id"
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(f"Product: {record[0]}, Supplier: {record[1]}")
        print()

    db.close()


# Modify your module database so that it contains an additional function named display_product_supplier_locations.
# This function should take no parameters and should display each product with its supplier and the location of the
# supplier. You should use suitable multiple inner joins to query the database.

def display_product_supplier_locations():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name, location.city, location.country  " \
          "FROM product " \
          "INNER JOIN supplier ON product.supplier_id = supplier.id  " \
          "INNER JOIN location ON supplier.location_id = location.id"
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(f"Product: {record[0]}, Supplier: {record[1]}, Supplier Location: {record[2]}, {record[3]}")
        print()

    db.close()



