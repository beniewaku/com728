#ask user to enter the book cover type
print("what type of cover does the book have (hard or soft)?")
cover_type = input()
#display suitable message
if cover_type == "soft":
    print("is the book perfect-bound?")
    perfect_bound = input()

    if perfect_bound == "yes":
        print("soft cover, perfect-bound books are very popular!")
    else:
        print("soft covers with coils or stitches are great for short books")
else:
    print("books with hard covers can be more expensive!")