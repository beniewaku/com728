print("What is your name human?")
name = input()

print("How old are you (in years)?")
age = int(input())

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = float(input())

print("calculating bmi")
bmi = weight / (height ** 2)

print(f"your bmi is {bmi: .2}")


def run():
    return None