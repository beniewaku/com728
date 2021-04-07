#display the message
print("What strange markings do you see?")
markings = input()

#identify the markings
print("\n identifying ...\n")

for count in range(0, len(markings),1):
  print(f"index {count}:", markings [count])