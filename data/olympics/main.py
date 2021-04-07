import csv
import process
import tui

# Replace the keyword pass for the function read_data with code to read the specified file_path
# display the message "Reading data from {file_path}" where {file_path}is the value of the parameter.
# Read the content of the CSV file line by line and store each line in a local list named data
# You should ignore the first line which contains the headings.
# Use the appropriate method from the module tui to indicate that the operation has completed.
# Return the list data.
def read_data(file_path):
    tui.started(f"Reading data from {file_path}")
    data = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            data.append(line)
    tui.completed()
    return data


def run():
    athlete_data = read_data("athlete_events.csv")
    # The run function also contains the keywords pass.
    # These should be replaced with appropriate calls to the functions in the module process once this has been implemented

    while True:
        selection = tui.menu()
        if selection == "years":
            process.list_years(athlete_data)
        elif selection == "tally":
            process.tally_medals(athlete_data)
        elif selection == "team":
            process.tally_team_medals(athlete_data)
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()