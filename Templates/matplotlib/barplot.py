import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting side by side bars, each pair sharing one label
labels = ['A', 'B', 'C', 'D']
y1 = [3.2, 4.5, 2.8, 5.1]
y2 = [2.7, 5.0, 3.9, 4.2]

x = np.arange(len(labels))  # one slot per label
width = 0.35                # bar width, the offset is half of it

fig, ax = plt.subplots()
ax.bar(x - width / 2, y1, width, label='control', color='steelblue')
ax.bar(x + width / 2, y2, width, label='treated', color='indianred')

ax.set_xticks(x, labels=labels)  # tick in the middle of each pair
ax.set_title('Grouped bar plot')
ax.set_xlabel('group')
ax.set_ylabel('value')
ax.set_axisbelow(True)  # grid behind the bars
plt.legend(frameon=False, loc='upper left')
plt.show()
plt.close()
