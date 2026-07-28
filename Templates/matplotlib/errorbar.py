import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting measurements with error bars
x = np.arange(1, 9)
y = np.sqrt(x)
yerr = 0.1 * np.sqrt(x)

fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=yerr, fmt='o-', color='steelblue', capsize=4,
            markersize=5, label=r'$\sqrt{x} \pm \sigma$')

ax.set_title('Error bars')
ax.set_xlabel('x values')
ax.set_ylabel('measurement')  # pass xerr= as well for horizontal bars
plt.legend(frameon=False, loc='upper left')
plt.show()
plt.close()
