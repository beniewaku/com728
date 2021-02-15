#ask user what cocktail they like
print("what cocktail do you like?")
cocktail = input()

#ask user if they like ice with it
print("Do you like it with a lot of ice or less ice or no ice?")
ice_preference = input ()

#ask user how they like their cocktail
print("do you like your drinks strong or sweet?")
taste = input()

#determine what user likes
if (ice_preference == "less ice") or (ice_preference == "lots of ice") or (ice_preference == "no ice"):
    print("oh that's good!")

elif ice_preference == "i don't like ice":
        print("that's interesting!")

elif (taste == "strong") or  (taste == "sweet") or (taste == "bitter") or (taste == "spicy"):
    print("that is the perfect balance!")

    if (taste == "bitter") or ("spicy"):
        print("that is a very strong cocktail")
else:
        print("everyone's got their own preference")

