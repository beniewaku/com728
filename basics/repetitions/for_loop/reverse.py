#display the phrase
print("What phrase do you see?")
phrase = input()

#identify phrase
print("\n reversing phrase ...")
print("The phrase is:", end="")

for position in range(len(phrase)-1,-1, -1):
    print(phrase[position],end="")