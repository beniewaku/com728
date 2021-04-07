def search (file_name):
    print("searching...")
    with open(file_name) as file:
        for location in file:
            print(f"Looked in {location} is a line from the file")
            print("...Done!")

def run():
    search("library.txt")

if __name__ == "__main__":
  run()
