import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on making a simple animation: a travelling sine wave
x = np.linspace(0, 10, 400)

fig, ax = plt.subplots()
line, = ax.plot([], [], color='steelblue', linewidth=2)
ax.set_xlim(0, 10)      # an animated axis does not autoscale, set the limits by hand
ax.set_ylim(-1.2, 1.2)
ax.set_title('Travelling wave')
ax.set_xlabel('x values')
ax.set_ylabel('y values')


def update(frame):
    line.set_data(x, np.sin(x - 0.1 * frame))  # only the data changes, never the artist
    return (line,)


# keep the object in a variable, otherwise it is garbage collected and the animation freezes
ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)

# ani.save('wave.gif', writer='pillow', fps=30)
plt.show()
plt.close()
