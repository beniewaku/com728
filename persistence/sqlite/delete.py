import sqlite3

# The first function should be named get_bot_id_from_user and should take no parameters.
# The function should ask the user to enter a bot id and return the value entered by the user.

def get_bot_id_from_user():
    print("Please enter a bot id:")
    return int(input())

# The second function should be named remove_bot_from_db and should have one parameter which is an integer
# representing a bot id. The function should remove the record related to the bot id from the database and display
# the record.

def remove_bot_from_db(bot_id):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    values = [bot_id]

    sql = f"SELECT * FROM bots WHERE id={id}"
    cursor.execute(sql)
    record = cursor.fetchone()
    print(f"The following record has been found:\n{record}")

    sql = f"DELETE FROM bots WHERE id= {id}"
    cursor.execute(sql)
    db.commit()
    print("The record has been removed.")

    db.close()



# The final function should be named run and should take no parameters.
# This function should call the earlier functions and display suitable output


def run():
    bot_id = get_bot_id_from_user()
    remove_bot_from_db(bot_id)


if __name__ == "__main__":
    run()