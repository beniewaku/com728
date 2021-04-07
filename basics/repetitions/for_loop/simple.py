print("How many mountains should I display?")
number_of_mountains = int(input())

#display mountains
print("Displaying mountains ...")

for number_of_mountains in range (number_of_mountains):
    print("""
    __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\
    
    """)

print("done! Mountains displayed")
