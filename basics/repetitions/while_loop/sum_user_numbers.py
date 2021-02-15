#display the message
print("How many numbers should i sum up?")
sum_of_numbers = int(input())

#variable
sum = 0

print()

#total of summed number
total = 0

while sum < sum_of_numbers:
    print(f"please enter a number {sum} of {sum_of_numbers}:")
    number = int(input())
    total = total + number
    sum = sum + 1
print(f"the answer is {total}")