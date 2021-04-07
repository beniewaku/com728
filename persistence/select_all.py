# Create a program that has the following functions:
# A function named retrieve_bots that has no parameters.
import sqlite3


def retrieve_bots():
    db = sqlite3.connect("../../persistence/sqlite/bots.db")
    cursor = db.cursor()
    # The function should connect to the database.

    sql = "SELECT * FROM bots;"
    cursor.execute(sql)

# The function should then retrieve all the records stored in the table bots.
# The function should then display each record in retrieved records on a new line.

    records = cursor.fetchall()


    for record in records:
        print(record)

    db.close()
# Finally, the function should close the database.


# A function named run which calls the function retrieve_bots and suitably displays the output

def run():
    retrieve_bots()

if __name__ == "__main__":
    run()

