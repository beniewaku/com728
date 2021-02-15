#ask for direction
print("towards which direction should i paint in (up, down, left or right)?")
direction =input()

#ask which direction they paint towards
if direction == "up":
    print("I am painting towards the upward direction!")
elif direction == "down":
    print("i am painting towards the downward direction")
elif direction == "left":
    print("i am painting towards the left direction")
elif direction == "right":
    print("i am painting towards the right direction")
else:
    print("i don't know where to paint")