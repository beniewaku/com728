# write a program that will allow us to load the data set for processing

# Write a variable named records set to an empty list
# Write a variable named headings set to an empty list
import csv

import records as records

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
# add option [5] display the number of survivors per age group  to the menu
def display_menu():
    print(
        """
        Please select one of the following options"
        [1] Display the names of all passengers
        [2] Display the number of passengers that survived
        [3] Display the number of passengers per gender
        [4] Display the number of passengers per age group
        [5] Display the number of survivors per age group

        """)

    # function should read in user's response as an integer
    return int(input())


# display the function name display message with no parameters
# display message the names of the passengers are
def display_passenger_names():
    print("The names of the passengers are ...\n")
    for record in records:
        passenger_names = records[3]
        print(passenger_names)


# display the function display number of survivors with no parameters
# function should create a local variable named num survived
def display_num_survivors():
    num_survived = 0

    for record in records:
        survival = int(record[1])
        if survival == 1:
            num_survived += 1

    print(f"{num_survived} passengers survived")


# contain the function display passengers per gender with no parameters
# create a local variable named females with the value 0
# create a local variable named males with the value 0
def display_passengers_per_gender():
    females = 0
    males = 0
    # retrieve values corresponding to the gender and store it in a variable named gender
    for record in records:
        gender = record[4]
        if gender.lower() == "male":
            males += 1
        else:
            females += 1
    print(f"Females: {females}, Males: {males}")


# contain the function display passengers per age group with no parameters
# create three local variables children, adults and elderly and set to 0
def display_passengers_per_age():
    children = 0
    adults = 0
    elderly = 0
    # for each record in global variable records retrieve the vale to the age and store it in a variable named age
    for record in records:
        if record[5] != "":
            age = float(record[5])
        if children < 18:
            children += 1
        elif adults < 65:
            adults += 1
        else:
            elderly += 1
    print(f"Children: {children}, Adults: {adults}, Elderly: {elderly}")


# add a function named display survivors per age group
def display_num_survivors_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    child_survivors= 0
    adult_survivors = 0
    elderly_survivors = 0

    # calculate and display number of passengers that survived for each age group
    for record in records:
        survived = int(record[1])
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
                if survived == 1:
                    child_survivors += 1
            elif age < 65:
                adults += 1
                if survived == 1:
                    adult_survivors += 1
            else:
                elderly += 1
                if survived == 1:
                    elderly_survivors += 1

    print(f"children:{child_survivors}/{children}, adults: {adult_survivors}/{adults}, elderly: {elderly_survivors}/{elderly}")


# Display the function run with no parameters
def run():
    # call the function load_data with the value for file_path
    load_data("Titanic.csv")
    # display message "successfully loaded {num_records} records"
    print(f"Successfully loaded {len(records)} records")

    selected_option = display_menu()
    print(f"You have selected option: {selected_option}\n")

    # if user enters option 1 display passenger names
    # if user enters number other than 1 display error message

    # update run function if user selects option 2
    # call the function display_num_survivors

    # update run function if user selects option 5
    # call the function

    display_passenger_names()
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age()
    elif selected_option == 5:
        display_num_survivors_per_age_group()
    else:
        print("Error! option not recognised!")


# update the run function
# if option 3 is selected function should call display passengers per gender

# update the run function
# if option 4 is selected call the fucntion display passengers per age group


if __name__ == "__main__":
    run()
