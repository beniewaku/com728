import json


def read(file_path):
    with open(file_path) as file:
        data = json.load(file)

        city = data["city"]
        print(f"City Name: {city}")

        population = data["population"]
        print(f"Population Size: {population}")

        for bot in data["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")


def run():
    read("robocity.json")
