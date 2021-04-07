#create a program to help Beep and Bop decipher the pattern.
#The program should consist of the following two functions

#The first function should be named pattern and should have no parameters.
def pattern():
    sequences = {"short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences

#The function should create a dictionary named sequences.
#The function should populate the dictionary with the following items: "Short Sequence":3, "Medium Sequence":2, "Long Sequence":1
#the function should return the dictionary

#The second function should be named run and should have no parameters.
#The function should call the first function and display the dictionary returned by the call.
def run():
    print(pattern())

if __name__ == "__main__":
    run()
