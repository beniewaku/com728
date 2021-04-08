import sqlite3


# The first function should be named get_bot_id_from_user and take no parameters
# The function should ask the user to enter a bot id and return the value entered by the user.

def get_bot_id_from_user():
    print("Please enter a bot id:")
    return int(input())


# The second function should be named display_bot_from_db and should have one parameter which is an integer
# representing a bot id.
# The function should retrieve the record related to the bot id from the database and display the record.

def display_bot_from_db(bot_id):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = f"SELECT * FROM bots WHERE id={id}"
    values = [bot_id]
    cursor.execute(sql)
    record = cursor.fetchone()
    db.close()

    print(record)


# The third function should be named get_bot_details_from_user and should take no parameters. The
# function should ask the user to enter the name of field to be updated and the new value for the field. The function
# should return a list containing the name of the field and its value.

def get_bot_details_from_user():
    print("Which field would you like updated?")
    field = input()
    print("Insert new value")
    value = input()

    return [field, value]


# The fourth function should be named update_bot_in_db and should take two parameters which represent the bot id and
# bot details. The function should update the relevant record in the database using the bot id and bot details.

def update_bot_in_db(bot_id, data):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = "UPDATE bots SET ?=? WHERE id=?"
    values = [data[0], data[1], bot_id]
    cursor.execute(sql, values)
    db.commit()
    db.close()

    print("Updated")


# The final function should be named run and should take no parameters.
# This function should call the earlier functions and display suitable output


def run():
    bot_id = get_bot_id_from_user()
    display_bot_from_db(bot_id)

    data = get_bot_details_from_user()
    update_bot_in_db(bot_id, data)

if __name__ == "__main__":
    run()


