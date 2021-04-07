def gang():
   print("Loading gang ...")
   friends = ["Scooby Doo", "Shaggy Rogers", "Fred Jones", "Daphne Blake", "Velma Dinkley"]
   return friends


def run():
    print(gang())
    print("Done!")
run()

# Function: phrases
#
# Requirements:
# [1] The function should be named phrases.
# [2] The function should have 1 parameter named friends which represents a list of friends.
def phrases(friends):
    quotes = {}
    for friend in friends:
        print(f"What does {friends} say?")
        response = input()
        quote = response

# [3] The function should start by creating a dictionary named quotes.
# [4] For each friend in the list friends, the function should do the following:
# [5]     Display the message "What does {friend} say?" where {friend} is the name of the friend.
# [6]     Read in the user's response and store it in a variable named quote.
# [7]     Add the value assigned to quote to the dictionary quotes using the friend's name as a key.
# [8] Finally, the function should return the dictionary quotes.
#
# A suitable call to the function are given below. This can be used to execute the function.
#
# friends = gang()
# quotes = phrases(friends)
# print(f"\nPhrases: {quotes}\n")