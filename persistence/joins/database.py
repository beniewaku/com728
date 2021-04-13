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
