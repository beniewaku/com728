def directions():
    directions = ["Move forward", "Move backward","Turn left", "Turn right"]
    return directions
def menu():
    print("Please select a direction:")
    direc = directions()
    for index in range(len(direc)):
        print(f"{index}: {direc}")
        #print("{index}: {index}
    index = int(input())
    return direc[index]


def run():
    route = []
    print("Working out display route:...")
    for count in range(5):
        route.append(menu())
        print(f"Escape route: {route}")
run()

