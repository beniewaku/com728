#ask how many bars are charged
print("How many bars should be charged?")
bars_to_charge = int(input())

#variable
bars_charged = 0

#bars displayed
print()

while bars_charged < bars_to_charge:
    bars_charged = bars_charged + 1
    print(f"Charging: {'█' * bars_charged}")
print("The battery is fully charged")