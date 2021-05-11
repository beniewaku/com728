import csv
import matplotlib.pyplot as plt


def read_data():
    with open("temps.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        data = {'week 1': [], 'week 2': []}
        for line in csv_reader:
            data["week 1"].append(float(line[0].strip()))
            data["week 2"].append(float(line[1].strip()))
    return data


def run():
    data = read_data()
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data['week 1'])), data['week 1'])
    ax2.plot(range(len(data['week 2'])), data['week 2'])
    plt.tight_layout()
    plt.show()

run()
