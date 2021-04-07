# write a program that will allow us to load the data set for processing

# Write a variable named records set to an empty list
# Write a variable named headings set to an empty list
import csv

records = []
headings = []


# display function load_data with one parameter file_path
# display loading data
def load_data(file_path):
    print("Loading data ...")
    # function should open the file given by file_path for reading using module csv
    # read in the first line of the file and assign it to the headings variable
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        # read in the list of values and add to the records variable

        for line in csv_reader:
            records.append(line)

    print("Done!")


# modify our existing program
# contain the function display_menu with no parameters
# display the message
def display_menu():
    print(
        """
        Please select one of the following options"
        [1] Display the names of all passengers
        [2] Display the number of passengers that survived
        [3] Display the number of passengers per gender
        [4] Display the number of passengers per age group

        """)

    # function should read in user's response as an integer
    return int(input())

#display the function name display message with no parameters
#display message the names of the passengers are
def display_passenger_names():
    print("The names of the passengers are ...\n")
    for record in records:
        passenger_names = records [1]
        print(passenger_names)

# Display the function run with no paramenters
def run():
    # call the function load_data with the value for file_path
    load_data("Titanic.csv")
    # display message "successfully loaded {num_records} records"
    print(f"Successfully loaded {len(records)} records")

    selected_option = display_menu()
    print(f"You have selected option: {selected_option}\n")

    # if user enters option 1 display passenger names
    # if user enters number other than 1 display error message
    display_passenger_names()
    if selected_option == 1:
        display_passenger_names()
    else:
        print("Error! option not recognised!")

if __name__ == "__main__":
    run()


if __name__ == "__main__":
    run()
