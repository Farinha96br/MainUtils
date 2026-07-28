import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting a scatter plot with dots
rng = np.random.default_rng(0)
x1, y1 = rng.normal(0, 1, 200), rng.normal(0, 1, 200)
x2, y2 = rng.normal(2, 1, 200), rng.normal(1, 1, 200)

fig, ax = plt.subplots()
ax.scatter(x1, y1, s=25, color='steelblue', alpha=0.7, edgecolors='none', label='group 1')
ax.scatter(x2, y2, s=25, color='indianred', alpha=0.7, edgecolors='none', label='group 2')

ax.set_title('Scatter plot')
ax.set_xlabel('x values')
ax.set_ylabel('y values')
plt.legend(frameon=False, loc='upper left')
plt.show()
plt.close()
