# enter first whole number
print("enter the first whole number")
first_number = int(input())
print()
# enter second whole number
print("enter the second whole number")
second_number = int(input())
# enter third whole number
print("enter the third whole number")
third_number = int(input())

even_numbers = 0
odd_numbers = 0

# which numbers are odd or even
if first_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if second_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if third_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
# display result
print(f"there are {even_numbers} even and {odd_numbers} odd")
