#display sequence of characters
print("Enter sequence of characters:")
sequence = input()

#display character of markers
print("enter characters for markers:")
marker = input()

#find the markers
marker1_position = -1
marker2_position = -1

for position in range(0,len(sequence),1):
    letter = sequence[position]
    if letter == marker:
        if (marker1_position == -1):
            marker1_position = position
        else:
            marker2_position = position
#result
print(f"the distance between the markers are {marker2_position - marker1_position - 1}.")
