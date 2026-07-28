import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting a histogram of two overlapping samples
rng = np.random.default_rng(0)
a = rng.normal(0, 1, 1000)
b = rng.normal(1.5, 1.2, 1000)

bins = np.linspace(-4, 6, 40)  # shared bins so the two are comparable

fig, ax = plt.subplots()
ax.hist(a, bins=bins, color='steelblue', edgecolor='black', alpha=0.6, label='sample A')
ax.hist(b, bins=bins, color='indianred', edgecolor='black', alpha=0.6, label='sample B')

ax.set_title('Histogram')
ax.set_xlabel('value')
ax.set_ylabel('count')  # use density=True above for a normalized histogram
ax.set_axisbelow(True)
plt.legend(frameon=False, loc='upper right')
plt.show()
plt.close()
