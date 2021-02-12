#ask user for the direction
print("towards which direction should i paint (up, down, left or right)?")
direction = input()

#which message to display
if direction == "up":
    print("i am painting in the upward direction!")
elif direction == "down":
    print(" i am painting in the downward direction!")
elif direction == "left":
    print("i am painting towards the left")
elif direction == "right":
    print("i am painting towards the right")
else:
    print("not sure which direction to paint in")
