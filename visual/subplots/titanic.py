import csv
import matplotlib.pyplot as plt


def read_data():
    with open('titanic.csv') as file:
        csv_reader = csv.reader(file)
        data = {'survived': [], 'sex': [], 'age': [], 'fare': []}
        for line in csv_reader:
            survived = line[1].strip()
            sex = line[14].strip()
            age = line[4].strip()
            fare = line[8].strip()
