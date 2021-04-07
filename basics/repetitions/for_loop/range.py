#display the message
print("What level of brightness is required?")
brightness_level = int(input())

#adjusting brightness level
print("\n Adjusting brightness...")

for brightness_level in range (2, brightness_level +1, 2):
    print(f"beep's brightness level: {'*'* brightness_level}")
    print(f"bop's brightness level: {'*'* brightness_level}")
print("adjustments completed!")