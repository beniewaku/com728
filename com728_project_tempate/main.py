"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, querying of the database and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module tui
        any processing should be done using the appropriate functions in the module process
        any database related querying should be done using the appropriate functions the module database
        any visualisation should be done using the appropriate functions in the module visual
"""

# Task 19: Import required modules
# TODO: Your code here
import csv
import process
import tui

# Task 20: Create an empty list named 'records'.
# This will be used to store the data read from the source data file.
# TODO: Your code here
import visual

records = []


def run():
    # Task 21: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()

    while True:
        # Task 22: Use the appropriate function in the module tui to display the main menu
        # and retrieve the user's desired selection.
        # This should be assigned to a suitable local variable
        # You should remove the keyword pass below before you start this task

        # TODO: Your code here
        selection = tui.main_menu()

    # Task 23: Check if the user selected the option for loading data.
    # If so, then do the following:
    # - Use the appropriate function in the module tui to display a message to indicate that the
    # data loading operation has started.
    # - Load the data by doing the following:
    #   - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.
    #   - Read each line from the CSV file (as a list of values) and add it to the list 'records'.
    # - Use the appropriate function in the module tui to display a message to indicate that the
    # data loading operation has completed.
    # TODO: Your code here

        if selection == 1:
            tui.started(operation="Loading data")

        file_path = tui.data_file_path()
        with open(file_path) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            records = list(csv_reader)

        print(records)

        tui.completed(operation="Loading data")


    # Task 29: Check if the user selected the option for processing data.
    # If so, then do the following:
    # - Use the appropriate function in the module tui to display a message to indicate that the
    # data processing operation has started.
    # - Process the data by doing the following:
    #   - call the appropriate function in the module tui to determine what processing is to be done.
    #   - call the appropriate function in the module process and display the results
    # - Use the appropriate function in the module tui to display a message to indicate that the
    # data processing operation has completed.

    elif selection == 2:
    tui.started(operation="Data loading operation")
    selection = tui.process_menu()

    if selection == 1:
        process.individual_movie(records)
    elif selection == 2:
        process.individual_movie(records)
    elif selection == 3:
        process.specific_individual_movie(records)
    elif selection == 4:
        process.specific_release_year(records)
    elif selection == 5:
        process.specific_genre(records)

    tui.completed(operation = "data processing operation")



    # Task 36: Check if the user selected the option for setting up or querying the database.
    # If so, then do the following:
    # - Use the appropriate function in the module tui to display a message to indicate that the
    # database querying operation has started.
    # - Query the database by doing the following:
    #   - call the appropriate function in the module tui to determine what querying is to be done.
    #   - call the appropriate function in the module database and display the results
    # - Use the appropriate function in the module tui to display a message to indicate that the
    # database querying operation has completed.

    elif selection == 3:
    tui.started("database querying operation")
    selection = tui.database_menu()

    if selected_option_database_menu == 1:
        setup(records)
    elif selected_option_database_menu == 2:
        result = all_directors()
        print(result)
    elif selected_option_database_menu == 3:
        result = top_5_movies()
        display_query_results(result)
    elif selected_option_database_menu == 4:
        result = top_5_movies_per_country()
        display_query_results(result)
    elif selected_option_database_menu == 5:
        result = top_5_movies_per_country_for_genre()
        display_query_results(result)
    elif selected_option_database_menu == 6:
        result = specific_actor()
        display_query_results(result)

    completed("database querying operation")





    # Task 40: Check if the user selected the option for visualising data.
    # If so, then do the following:
    # - Use the appropriate function in the module tui to indicate that the data visualisation operation
    # has started.
    # - Visualise the data by doing the following:
    #   - call the appropriate function in the module tui to determine what visualisation is to be done.
    #   - call the appropriate function in the module visual
    # - Use the appropriate function in the module tui to display a message to indicate that the
    # data visualisation operation has completed.

    elif selection == 4:
    completed('data visualisation operation')
    selection = tui.visual_menu()

    if selection == 1:
        visual.display_total_no_of_movies_in_each_genre()
    elif selection == 2:
        visual.display_total_no_of_movies_per_country()
    elif selection == 3:
        visual.display_top_movies_per_country_for_genre()

    completed("database querying operation")

    # Task 41: Check if the user selected the option for exiting the program.
    # If so, then break out of the loop
    # TODO: Your code here

    elif selection == 5:
    break



    # Task 42: If the user selected an invalid option then use the appropriate function of the
    # module tui to display an error message
    # TODO: Your code here
    else:
     error('Please select the correct option from main menu')


if __name__ == "__main__":
    run()

