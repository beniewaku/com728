import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

line = None
boxes = []


def init():
    global boxes
    boxes.append({'x': [2, 2, 3, 3, 2], 'y': [2, 3, 3, 2, 2]})
    boxes.append({'x': [2, 2, 5, 5, 2], 'y': [2, 5, 5, 2, 2]})
    boxes.append({'x': [1, 1, 8, 8, 1], 'y': [1, 8, 8, 1, 1]})


def animate(frame):
    global boxes, line
    box_index = frame % 3
    line.set_data(boxes[box_index]['x'], boxes[box_index]['y'])


def run():
    global line
    fig, ax = plt.subplots()
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 7)
    line, = ax.plot([], [], linewidth=4)
    sine_animation = animation.FuncAnimation(fig, animate, frames=3, interval=1000, init_func=init)
    plt.show()


run()
