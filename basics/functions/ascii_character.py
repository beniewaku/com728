#display the message to start the program
print("Program started!")
print("Please enter a Ascii code")
code = abs(int(input()))

#check the number is in range within 32-126
if code in range(32, 126):
    print(f"The character represented by the ascii code {code} is: {chr(code)}")
else:
  print("character error")

print("program ended!")
