def listen():
    print("what sound did you hear?")
    sound = input()
    print(f"That was a loud {sound}!")
listen()

def voyage(distance):
    for distance in range(distance):
        print("...crossed some ocean")
voyage(3)
print("you have found maui on the island")