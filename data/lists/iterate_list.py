def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  direc = directions()
  for index in range(len(direc)):
    print(f"{index}: {direc[index]}")

def run():
  menu()

run()