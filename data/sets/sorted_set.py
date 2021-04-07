#Create a variation of our previous program to help Beep and Bop record their observations.
#first function should be named observed and should have no parameters.

def observed():
    observations = []
    for _ in range(5):
        print("State your observations:")
        observation = input()
        observations.append(observation)
    return observations

#The function should create a list named observations.
#The function should populate the list with 5 values read in from the user.  There should be some duplicate values.
#Finally, the function should return the list named observations.


#The second function should be named remove_observations and should take 1 parameter.
#The parameter should represent the list of observations.
def remove_observations(observations):
    is_working = True
    while is_working:
        print("Do you wish to remove an observation?")
        response = input()
        if response.lower() == "yes":
            print("Enter observation:")
            observation = input()
            observations.remove(observation)
        else:
            is_working = False
#The function should ask the user if they wish to remove observations.

#The third function should be named run and should have no parameters.
#The function should call the first function and store the returned list in a local variable.
#The function should then call the second function with the previously retrieved list.
#Finally, the function should display a sorted set of the observations and how many times each observation has been made.

def run():
    observations_list = observed()
    remove_observations(observations_list)

    observations_set = set()

    for observation in observations_list:
        observation_tuple = (observation, observations_list.count(observation))
        observations_set.add(observation_tuple)

    print(sorted(observations_set))

if __name__ == "__main__":
    run()
