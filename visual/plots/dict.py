import matplotlib.pyplot as plt
import random as rnd


def data():
    paths = {}
    print("Please choose what type of line you would like (:, -- or -)?")
    line_type = input()
    print("Select a colour (r, g, or b)?")
    colour_choice = input()
    print("Select your marker (o, s, or ^)?")
    marker = input()

    paths['line_type'] = line_type
    paths['colour_choice'] = colour_choice
    paths['marker'] = marker
    return paths


def generate():
    print("Please enter how many lines you would like to display?")
    lines = int(input())

    for lines in range(lines):
        values = data()
        x = rnd.sample(range(1, 20), 5)
        y = rnd.sample(range(1, 20), 5)
        form = (f"{values['colour_choice']}{values['line_type']}{values['marker']}")
        plt.plot(x, y, form)
        plt.show()


def run():
    print("Running...")
    generate()
    print("Done")

run()
