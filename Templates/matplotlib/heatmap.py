import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': False,  # gridlines over an image are just noise
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting a heatmap with the value written on every cell
rows = ['A', 'B', 'C', 'D']
cols = ['w', 'x', 'y', 'z']
data = np.random.default_rng(0).random((len(rows), len(cols)))

fig, ax = plt.subplots()
im = ax.imshow(data, cmap='viridis')
fig.colorbar(im, ax=ax, label='value')

ax.set_xticks(np.arange(len(cols)), labels=cols)
ax.set_yticks(np.arange(len(rows)), labels=rows)

# write each cell value on top of its cell
for i in range(len(rows)):
    for j in range(len(cols)):
        ax.text(j, i, f'{data[i, j]:.2f}', ha='center', va='center', color='white')

ax.set_title('Heatmap with annotated cells')
ax.set_xlabel('columns')
ax.set_ylabel('rows')
plt.show()
plt.close()
