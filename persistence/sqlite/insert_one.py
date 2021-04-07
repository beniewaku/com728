# The first function should be named get_bot_from_user and should have no parameters.
# The function should ask the user to enter the data for a single bot and return a list containing the data.

import sqlite3


def get_bot_from_user():
    print("Please enter Bot name:")
    name = input()
    print("Please enter Bot speed:")
    speed = int(input())
    print("Please enter Bot strength:")
    strength = int(input())
    print("Please enter creation date:")
    date = input()
    print("Please enter manufacturer:")
    manufacturer = int(input())

    return [name, speed, strength, date, manufacturer]


# The second function should be named insert_bot_in_db and should take a single parameter which is a list containing
# bot details. The function should insert the data in the list as a new record into the table bots. The function
# should display the id of the newly inserted record.


def insert_bot_in_db(data):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = "INSERT INTO bots \
    (name, max_speed, max_strength, creation_date, manufacturer_id)" \
    "VALUES" \
     f"('{data [0]}', {data [1]}, {data [2]}, '{data [3]}', {data [4]})"

    cursor.execute(sql)

    row_id = cursor.lastrowid
    db.close()

    print(f"Display new id: {row_id}")

# The third function should be named run and should take no parameters.
# This function should call the earlier two functions and display suitable output

def run():
    data = get_bot_from_user()
    insert_bot_in_db(data)

if __name__ == "__main__":
    run()
