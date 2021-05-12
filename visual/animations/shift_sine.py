import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

line = None


def animate(frame):
    global line
    x = np.arange(0, (2 * np.pi), 0.01)
    y = np.sin(x + (frame / 50))
    line.set_data(x, y)


def run():
    global line
    fig, ax = plt.subplots()
    ax.set_xlim(0, (2 * np.pi))
    ax.set_ylim(-1, 1)
    line, = ax.plot([], [], linewidth=6)
    sine_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100)
    plt.show()


run()
