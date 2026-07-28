import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting a violin plot of three groups
rng = np.random.default_rng(0)
groups = [rng.normal(0, 1, 200), rng.normal(1, 1.5, 200), rng.normal(0.5, 0.7, 200)]
labels = ['A', 'B', 'C']

fig, ax = plt.subplots()
ax.violinplot(groups, showmedians=True)

ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)  # violin positions start at 1
ax.set_title('Violin plot')
ax.set_xlabel('group')
ax.set_ylabel('value')
ax.set_axisbelow(True)
plt.show()
plt.close()
