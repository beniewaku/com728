#enter adventure type
print("what type of adventure should i have?")
adventure_type = input()

#figure out which type of adventure
if (adventure_type == "scary") or (adventure_type == "short"):
    print("entering the dark forest!")
elif (adventure_type == "safe") or (adventure_type == "long"):
    print("Taking the safe route!")
else:
    print("not sure which route to take")