import action as action


def sum_weights(beep_weight, bop_weight):
    weight = beep_weight + bop_weight
    return weight
def calc_avg_weight(beep_weight, bop_weight):
    average_weight = (beep_weight + bop_weight) / 2
    return average_weight
def run():
    print("What is Beep's weight?")
    beep_weight = float(input())
    print("What is Bop's weight?")
    bop_weight = float(input())

    print("what would you like to calculate? (sum or average)?")
    action = input()

if action == "sum":
    answer = sum_weights("beep_weight, bop_weight")
    print(f"The sum of Beep's and Bop's weight is {answer:.2f}")
elif action == "average":
    answer = calc_avg_weight("beep_weight, bop_weight")
    print(f"The average of Beep's and Bop's weight is {answer:.2f}")
else:
    print("I am not sure what you would like to do.")
