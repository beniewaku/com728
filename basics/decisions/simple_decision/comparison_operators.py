#user enter the first number
print("please enter the first number")
first_number = int(input())

#user enter the second number
print("please enter the second number")
second_number = int(input())
#display smallest number
if first_number < second_number:
    print("first number is the smallest")
elif first_number > second_number:
    print("the second number is the smallest")
else:
    print("both numbers are equal")