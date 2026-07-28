import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting a 2x2 grid of panels
x = np.linspace(0, 10, 200)
series = [np.sin(x), np.cos(x), np.sin(x) * np.exp(-x / 5), np.sqrt(x)]
titles = [r'$\sin(x)$', r'$\cos(x)$', r'$\sin(x)e^{-x/5}$', r'$\sqrt{x}$']

fig, axes = plt.subplots(2, 2, figsize=(9, 6), sharex=True)
for ax, y, title in zip(axes.flat, series, titles):
    ax.plot(x, y, color='steelblue', linewidth=2)
    ax.set_title(title)

for ax in axes[-1]:      # x label only on the bottom row
    ax.set_xlabel('x values')
for ax in axes[:, 0]:    # y label only on the left column
    ax.set_ylabel('y values')

fig.suptitle('Grid of subplots')
fig.tight_layout()
plt.show()
plt.close()
