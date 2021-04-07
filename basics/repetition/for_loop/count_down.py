#display the message
print("How far are we from the cave?")
distance = int(input())

#count down the remaining steps
print()

for count in range(distance, 0, -1):
    print(f"{count} remaining steps")

print("We have reached the cave!")
