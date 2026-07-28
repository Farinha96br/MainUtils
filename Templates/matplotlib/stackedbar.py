import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting stacked bars
labels = ['A', 'B', 'C', 'D']
y1 = np.array([3.0, 4.0, 2.0, 5.0])
y2 = np.array([2.0, 1.5, 3.0, 1.0])
y3 = np.array([1.0, 2.5, 1.5, 2.0])

fig, ax = plt.subplots()
ax.bar(labels, y1, color='steelblue', label='part 1')
ax.bar(labels, y2, bottom=y1, color='indianred', label='part 2')
ax.bar(labels, y3, bottom=y1 + y2, color='darkseagreen', label='part 3')  # bottom = sum below

ax.set_title('Stacked bar plot')
ax.set_xlabel('group')
ax.set_ylabel('value')
ax.set_axisbelow(True)
plt.legend(frameon=False, loc='upper left')
plt.show()
plt.close()
