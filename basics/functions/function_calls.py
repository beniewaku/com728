def display_box(word):
    number_dashes = 6 + len(word)
    print("-"* number_dashes)
    print("| {word} |")
    print("|        |")
    print("-"* number_dashes)

def display_lower_case(word):
    print(word.lower())

def display_upper_case(word):
    print(word.upper())

def display_mirrored(word):
    mirrored = ""
    for mirrored in reversed(word):
        mirrored += word
    print(f"{word} | {mirrored}")

def display_repeated(word):
    print("How many times would you like the word repeated?")
    words_repeated = int(input())
    for words_repeated in range(words_repeated):
        if (words_repeated % 2 == 0):
            print("display lower case word")
        else:
            print("display upper case word")




def start():
    print("Key in a word")
    word = input()

    print("what option would you like to do?")
    print("[1]Display in a box")
    print("[2]Display lower case")
    print("[3]Display upper case")
    print("[4]Display mirrored")
    print("[5]Display repeated")
    print("[6] End restart")

    response = int(input())

    if response == 1:
        display_box(word)
    elif response == 2:
        display_lower_case(word)
    elif response == 3:
        display_upper_case(word)
    elif response == 4:
        display_mirrored(word)
    elif response == 5:
        display_repeated(word)
    else:
        print("Please start again")

start()
