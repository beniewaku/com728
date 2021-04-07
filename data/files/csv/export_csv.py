import csv

def export(file_path, bots_exported):
    print("Exporting...")
    with open("file path", "a")as file:
        for count in range(bots_exported):
            print("Enter in Bot id")
            bot_id = int(input())
            print("Enter in Bot name")
            bot_name = input()
            print("Enter in paint name for bot")
            bot_paint = input()

            data = f"{bot_id},{bot_name}, {bot_paint}\n"
            file.write(data)
        print("Done...!")

def run():
    export("exported_bots.csv", 2)


if __name__ == "__main__":
    run()