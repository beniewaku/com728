import random

print("please enter the minimum value")
min_value = int(input())

print("please enter maximum value")
max_value = int(input())

random_number = random.randrange(min_value,max_value)

print(f"i am thinking of a number between {min_value} and {max_value}")
print(f"can you guess what it is?")

guess_correct =False

while not guess_correct:
    print("enter a number")
    guess = int(input())

    if guess_correct == random_number:
        print("Congratulations! you guessed my number!")
        guess_correct = True
    elif guess < random_number:
        print("guess higher!")
    elif guess > random_number:
        print("guess lower")
    else:
        print("try again")

    print("Game over!")



