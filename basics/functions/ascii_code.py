#start the program
print("Program Started!")
print("Please enter a standard character")
character = input()

#check the length of the character
if len(character) == 1:
    print(f"The ascii code for {character} is {ord (character)}")
else:
    print("A single character was not entered")
print("Program ended!")