import csv

def read(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = csv_reader
        print(f"Headings:\n {headings}")

        print("Values:")
        for values in csv_reader:
            print(values)

def run():
    read("bots.csv")

if __name__ == "__main__":
  run()

x = int(input())
y = int(input())

x = x//y
y = y//x

print(y)