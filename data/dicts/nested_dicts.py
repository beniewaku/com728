# The first function should be named short_pattern and should have no parameters.
# The function should create a dictionary named pattern.
# The function should populate the dictionary with the following key-value pairs:
# "sequence":"101"
# "occurrences":5
# Finally, the function should return the dictionary.

def short_pattern():
    pattern = {
        "sequence":"101",
        "occurrence":5
    }
    return pattern

# The second function should be named medium_pattern and should have no parameters.
# The function should create a dictionary named pattern.
# The function should populate the dictionary with the following key-value pairs:
# "sequence":"111000"
# "occurrences": 25
# Finally, the function should return the dictionary

def medium_pattern():
    pattern = {
        "sequence": "111000",
        "occurrences": 25
    }
    return pattern

# The third function should be named long_pattern and should have no parameters.
# The function should create a dictionary named pattern.
# The function should populate the dictionary with the following key-value pairs:
# "sequence":"1100110011001100"
# "occurrences":50

def long_pattern():
    pattern = {
        "sequence": "1100110011001100",
        "occurrences": 50
    }
    return pattern




# The fourth function should be named run and should have no parameters.
# The function should start by displaying the message "Analysing patterns...".
# The function should then create a dictionary with the following key-value pairs:
# "short sequence": value returned from first function
# "medium sequence": value returned from second function
# "long sequence": value returned from third function

def run():
    print("Analysing patterns ...")
    patterns = {
        "short sequence": short_pattern(),
        "medium sequence": medium_pattern(),
        "long sequence": long_pattern()
    }
#the function should display the content of the dictionary as key-value pairs using an appropriate loop

    for key, value in patterns.items():
      print(f"{key}: {value}")

if __name__ == "__main__":
    run()
