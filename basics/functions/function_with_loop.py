def cross_bridge(steps):
    for steps in range(steps):
        print("Crossed steps")
    if steps > 5:
        print("bridge is collapsing")
    else:
        print("We must keep going!")
cross_bridge(3)
cross_bridge(6)