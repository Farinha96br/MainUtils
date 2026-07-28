import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': False,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting a filled contour of a 2d field
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2) / 2) * np.cos(2 * X)

fig, ax = plt.subplots()
filled = ax.contourf(X, Y, Z, levels=20, cmap='viridis')
fig.colorbar(filled, ax=ax, label=r'$z$')

lines = ax.contour(X, Y, Z, levels=6, colors='white', linewidths=0.8)
ax.clabel(lines, inline=True, fontsize=9)  # write the level on each line

ax.set_title('Filled contour with labelled levels')
ax.set_xlabel('x values')
ax.set_ylabel('y values')
ax.set_aspect('equal')
plt.show()
plt.close()
