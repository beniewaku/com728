def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("still some way to go!")
    else:
        print("we are almost there!")
climb_ladder(5, 2)
climb_ladder(2, 5)