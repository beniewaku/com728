# Create a program that has the following functions:
# A function named retrieve_bots and has 1 parameter which represents the number of bots to fetch from the database.
# The default value of the parameter should be None.

import sqlite3


# The function should connect to the database
def retrieve_bots(num_bots=None):
    db = sqlite3.connect("../../../persistence/sqlite/bots.db")
    cursor = db.cursor()

    sql = "SELECT * FROM bots;"
    cursor.execute(sql)

    # the parameter value is None then The function should retrieve all the records stored in the table bots. Otherwise,
    # if the parameter value is not None then The function should retrieve many records from table bots.  The number of
    # records retrieve should be equal to the value of the parameter. The function should then display each record
    # retrieved from the database on a new line.

    if num_bots == None:
        records = cursor.fetchall()

    else:
        records = cursor.fetchmany(num_bots)

    for record in records:
        print(record)

    db.close()
# Finally, the function should close the database.


# A function named run that calls the function retrieve_bots and suitably displays the output

def run():
    print("First three bots in the system:")
    retrieve_bots(3)

if __name__ == "__main__":
        run()
