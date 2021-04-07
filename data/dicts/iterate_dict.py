# The program should contain the functionality of the previous program.  Additionally, the program should contain the following functions:
def pattern():
    sequences = {"short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences

# A function named display_keys that takes a single parameter data which is a dictionary.
# The function should iterate through the keys of the dictionary and display each on a new line.

def display_keys(data):
    print("Keys:")
    for key in data:
        print(key)
    print()


# A function named display_values that takes a single parameter data which is a dictionary.
# The function should iterate through the values of the dictionary and display each on a new line.

def display_values(data):
    print("Values:")
    for value in data.values():
        print(value)
    print()


# A function named display_items that takes a single parameter data which is a dictionary.
# The function should iterate through each key-value pair and display it on a new line.
def display_pairs(data):
    print("Pairs:")
    for key, value in data:
        print(f"{key}: {value}")
    print()

# You should modify the function run so that it calls each of the functions described above.

def run():
    data = pattern()
    print(f"Dictonary:\n {data}")

    display_keys(data)
    display_values(data)
    display_pairs(data)


if __name__ == "__main__":
    run()
