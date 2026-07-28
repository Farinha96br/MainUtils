import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting a line with a shaded confidence band
x = np.linspace(0, 10, 200)
y = np.sin(x)
sd = 0.1 + 0.05 * x  # band half width, widening with x

fig, ax = plt.subplots()
ax.plot(x, y, color='steelblue', linewidth=2, label=r'$\sin(x)$')
ax.fill_between(x, y - sd, y + sd, color='steelblue', alpha=0.3, linewidth=0, label=r'$\pm\sigma$')

ax.set_title('Line with confidence band')
ax.set_xlabel('x values')
ax.set_ylabel('y values')
plt.legend(frameon=False, loc='upper right')
plt.show()
plt.close()
