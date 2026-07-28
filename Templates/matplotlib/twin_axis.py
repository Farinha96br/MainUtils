import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting two series with very different scales
x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = 1000 * np.exp(x / 5)

fig, ax = plt.subplots()
line1, = ax.plot(x, y1, color='steelblue', linewidth=2, label=r'$\sin(x)$')
ax.set_xlabel('x values')
ax.set_ylabel(r'$\sin(x)$', color='steelblue')
ax.tick_params(axis='y', labelcolor='steelblue')

ax2 = ax.twinx()  # shares the x axis, own y axis on the right
line2, = ax2.plot(x, y2, color='indianred', linestyle='--', linewidth=2, label=r'$1000e^{x/5}$')
ax2.set_ylabel(r'$1000e^{x/5}$', color='indianred')
ax2.tick_params(axis='y', labelcolor='indianred')
ax2.grid(False)  # one grid is enough

ax.set_title('Two y axes')
ax.legend(handles=[line1, line2], frameon=False, loc='upper left')  # one legend for both axes
plt.show()
plt.close()
