#ask the user for the place to look
print("where should i look?")
place = input()
#check the bedroom
if place == "bedroom":
    print("where in my bedroom should i look?")
    bedroom_place = input()
    if bedroom_place == "under the bed":
        print("found some shoes but no battery")
    else:
        print("found some mess but no battery")
#check the bathroom
elif place == "bathroom":
    print("where should i look?")
    bathroom_place = input()
    if bathroom_place == "in the bath tub":
        print("found a rubber duck but no battery")
    else:
        print("found some tools but no battery")
#check the lab
elif place == "Lab":
    print("where in the lab should i look?")
    lab_place = input()
    if lab_place == "on the table":
        print("Yes i found my battery!")
    else:
        print("found some tools but no battery")

else:
    print("i don't know where it is but i will keep looking")