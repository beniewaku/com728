#create a program to help Beep and Bop record what they can see in the distance.

#program should consist of the following two functions:

#The first function should be named observed and should have no parameters.
def observed():
    observations = {"flying Car", "Sky Scraper", "Laser", "Dome","Dome"}
    return observations
#The function should create a set named observations.
#The function should populate the list with the following items:
    #"Flying Car", "Sky Scraper", "Sky Scraper", "Laser", "Dome", "Dome"
# function should return the set observations.

def run():
    print(observed())

run()

#The second function should be named run and should have no parameters.
#The function should call the first function and display the set returned by the call.
