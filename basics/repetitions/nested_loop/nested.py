#display message
print("how many rows would you like?")
rows = int(input())
print("how many collumns would you like?")
collumns = int(input())

for rows in range (0, rows, 1):
    for columns in range(0, collumns, 1):
        print(":-)", end="")
    print()