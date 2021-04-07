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


if __name__ == "__main__":
    run()


