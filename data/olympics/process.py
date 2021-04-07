import csv
import tui

# - A function named started that takes 1 parameter named msg.  The default value of the parameter is an empty string.
# - The function should display a line of 85 dashes.
# - The function should then display the message
# "Operation started: {msg}...\n" where {msg} is the value passed as a parameter.


line_width = 85


def started(msg=""):
    output = f"Operation started: {msg}..."
    dashes = "-" * line_width
    print(f"{dashes}\n{output}\n")


# A function named completed that takes no parameters
def completed():
    dashes = "-" * line_width
    # The function should display a blank line followed by the message "operation completed"
    print(f"\nOperation completed.\n{dashes}\n")


# A new line with 85 dashes

def error(msg):
    print(f"Error!Invalid selection {msg}\n")


# A function named error that takes 1 parameter named msg.
# The function should display the message "Error! {msg}" where {msg} is the value passed as a parameter.

# A function named menu that takes no parameters
def menu():
    print(f"""
    Please select one of the following options:
    {"[years]":<10} List unique years
    {"[tally]":<10} Tally up medals
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the program
    """)
    selection = input("Your selection: ")
    return selection.strip().lower()

# The output should be suitably formatted to improve the appearance of the menu.  This can be done by using padding with the f-string.
# E.g. 1: print(f"{msg:10}") will display the value of msg.
# E.g. 2: print(f"{msg:<10}") will display the value of msg, align the text to the left and fill the remaining with spaces.
# E.g. 3: print(f"{msg:>10}") will display the value of msg, alight the text to the right and fill the remaining with spaces.
# - The function should return the selection (e.g. tally) entered by the user.


# A function named display_medal_tally which takes one parameter tally
# The parameter should have a dictionary that contains the keys and values Gold 10, Silver 5 & Bronze 2
def display_medal_tally(tally):
    tally = {"Gold": 10, "Silver": 5, "Bronze": 2}
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")
# - The function should display the name of each medal and its count with "Gold" displayed first and "Bronze" displayed last. Hint: No loop is required.

# A function named display_team_medal_tally with one parameter team_tally
def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")

# - The parameter team_tally is a nested dictionary. The keys of this dictionary are the names of each team.
# The values are a dictionary containing the names of medals and their counts e.g. {"United Kingdom", {"Gold": 10, "Silver": 5, "Bronze": 2}}.
# - The function should display the name of each team and the medals the team has one.

def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)

# A function named display_years that takes 1 parameter name years.
# The parameter years is a set containing integer values that for the years in which the Olympics were held.
# The function should sort the years into descending order (largest first) and display each year on a new line.

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





# We wish to implement the following functions:
import tui

col_medal = 14
col_team = 6
col_year = 9

# a function named list_years with one parameter data
# function should take a list named data as a parameter and extracts the set of distinct years
def list_years (data):
    data = []
    tui.started("Listing years")
    years = set()
    for record in data:
        year = record[col_year]
        years.add(year)
    tui.display_years(years)
    tui.completed()
# - The function should iterate through each record in the list and extract the year.
# - The function should add the extracted year to a local set so that we have a set of distinct years
# when the function finishes iterating through the list.
# - The appropriate functions from the module tui should be called to indicate the start of the operation, display the set of years and indicate the end of the operation.


# tally_medals(data): This function takes a list named data as a parameter and tallies up the number of gold, silver and bronze medals.
# - The function should create a dictionary that initially contains a count of zero for each medal i.e. {"Gold": 0, "Silver": 0, "Bronze": 0}.

def tally_medals(data):
    tui.started("Tallying medals")
    medals_tally = {"Gold: 0", "Silver: 0," "Bronze: 0"}
    # The function should iterate through each record in the list data and extract the medal.
    # If the medal is "Gold", "Silver" or "Bronze" then the relevant count in the dictionary should be incremented.
    for record in data:
        medal = record[col_medal]
        if medal in ("Gold", "Silver", "Bronze"):
            medals_tally[medal] += 1
    # The dictionary should contain the total count of each medal once the code has finished iterating through the list data.
    # The appropriate functions from the module tui should be called to indicate the start of the operation, display the tally of medals and indicate the end of the operation.
    tui.display_medal_tally(medals_tally)
    tui.completed()

# tally_team_medals(data): This function takes a list named data as a parameter and
# tallies up the number of gold, silver and bronze medals for each team.
# - The function will create a nested dictionary that contains the name of the team (the key)

def tally_team_medals(data):
    tui.started("Tallying medals for each team")
    medal_tally = {}
    for record in data:
        team = record[col_team]
        medal = record[col_medal]

        if medal not in ("Gold", "Silver", "Bronze"):
            continue

        if team in medal_tally:
            medal_tally[team][medal] += 1
        else:
            medal_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            medal_tally[team][medal] += 1

    tui.display_team_medal_tally(medal_tally)
    tui.completed()
# and a dictionary with the medals and their counts (the value) e.g. {"United Kingdom": {"Gold":10, "Silver":8, "Bronze":6}}
# - The function should initially create an empty dictionary.
# - The function should then iterate through each record in the list data and extract the name of the team and the medal.
# - The function should check if the team is already in dictionary.
# - If the team is already in the dictionary then
#         the function should retrieve the nested medals dictionary for that team and increment the appropriate count.
# - If the team is not already in the dictionary then
#         the function should add the team to the dictionary with the nested dictionary: {"Gold": 0, "Silver": 0, "Bronze": 0} as the value and increment the appropriate count.
# - The appropriate functions from the module tui should be called to indicate the start of the operation, display the tally of medals and indicate the end of the operation.

