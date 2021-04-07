#display the message
print("How many numbers should i sum up?")
max_numbers = int(input())

#variable to control the loop
count = 0

print()

#total of summed number
total = 0

while count < max_numbers:
    print(f"please enter a number {count + 1} of {max_numbers}:")
    number = int(input())
    total = total + number
    count = count + 1
print(f"the answer is {total}")