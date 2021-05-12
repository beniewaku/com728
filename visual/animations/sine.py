import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
line = None


def animate(frame):
    global ax
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    x_degrees = np.arrange(0, frame)
    x_radians = x_degrees * (np.pi / 180)
    y = np.sin(x_radians)
    ax.plot(x_degrees, y)


def run():
    global line
    sine_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100)
    plt.show()


run()
