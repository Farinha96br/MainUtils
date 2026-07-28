import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting a box plot of three groups
rng = np.random.default_rng(0)
groups = [rng.normal(0, 1, 200), rng.normal(1, 1.5, 200), rng.normal(0.5, 0.7, 200)]

fig, ax = plt.subplots()
ax.boxplot(groups, tick_labels=['A', 'B', 'C'], showmeans=True)

ax.set_title('Box plot')
ax.set_xlabel('group')
ax.set_ylabel('value')
ax.set_axisbelow(True)
plt.show()
plt.close()
