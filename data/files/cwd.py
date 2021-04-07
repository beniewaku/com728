import os
def cwd():
    path = os.getcwd()
    print(f"Current Working Directory: {path}")
    print("The directory contains the following files:")

    for file in os.listdir(path):
        print(file)

def run():
    print("Processing ...")
    cwd()


if __name__ == "__main__":
  run()