#ask user how many cables to remove
print("How many cables should i remove?")
cables_to_remove = int(input())

#create variable for removed variables
cables_removed = 0

#remove cables
print()

while cables_removed < cables_to_remove:
    print("removed cable.")
    cables_to_remove = cables_removed + 1
