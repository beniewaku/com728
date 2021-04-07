#display message
print("What phrase do you see?")
phrase = input()

#identifying markings
print("\n reversing phrase...\n")
print("The phrase is:", end="")

reversed= ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)