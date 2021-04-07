#create a program to help Beep and Bop record how many of each type of item they saw
#program should consist of the following two functions:
#The first function should be named observed and should have no parameters.
#The function should create a list named observations.
#The function should populate the list with 7 values read in from the user.  There should be some duplicate values.
#the function should return the list named observations.

def observed():
    observations = []
    for _ in range(7):
        print("State your observations")
        observation = input()
        observations.append(observation)
    return observations

#The second function should be named run and should have no parameters.
#The function should start by displaying the message "Counting observations...".
#The function should then call the first function and store the returned list in a local variable.
def run():
    print("Counting observations...")
    observations_list = observed()
    observations_set = set()

    for observation in observations_list:
        observation_tuple = (observation, observations_list.count(observation))
        observations_set.add(observation_tuple)


    print(observations_set)

if __name__ == "__main__":
    run()



# You can do this using the method count for a list.
    #For example, data.count("Sky Scraper") will return the number of times "Sky Scraper" appears in the list data.
#Finally, the function should display the content of the set.