# The first function should be named
# read_data_file and should take 1 parameter which is a file path. The function should read all the lines from the
# specified file and return them in a list.

import csv
import sqlite3


def read_data_file(file_path):
    data = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            data.append(line)
        return data

# The second function should be named insert_in_db and should take one
# parameter which is the list of data to be inserted.
# The function should insert each item (a record for a bot) from
# the list into the table bots.

def insert_in_db(data):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    for item in data:
        sql = "INSERT INTO bots " \
              "(name, max_speed, max_strength, creation_date, manufacturer_id)" \
              "VALUES" \
              f"('{item[0]}', {item[1]}, {item[2]}, '{item[3]}, {item[4]})"

        cursor.execute(sql)

        db.commit()
        db.close()


 # The final function should be named run and should take no parameters. The function
# should ask the user for a file path.
# The function should then call the earlier functions

def run():
    print("Enter file path")
    path = input()

    bots_data = read_data_file(path)

    print("Inserting to database...")
    insert_in_db(bots_data)
    print(f"Done! {len(bots_data)} records inserted.")



if __name__ == "__main__":
    run()
