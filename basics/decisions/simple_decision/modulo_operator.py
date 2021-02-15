#user to enter a whole number
print("please enter a whole number")
number = int(input())

#check if number is odd or even
if number %2 == 0:
    print(f"The number {number} is an even number")
else:
    print(f"The number {number}is an odd number")