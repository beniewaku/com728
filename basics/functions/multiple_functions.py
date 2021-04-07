def display_ladder(steps):
    for steps in range(steps):
        print("| |")
        print("***")
        print("| |")
def create_ladder():
    print("How many steps left?")
    remaining_steps = int(input())
    display_ladder(remaining_steps)
create_ladder()