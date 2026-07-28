import matplotlib.pyplot as plt
import numpy as np

USE_LATEX_STYLE = True

plt.rcParams.update({
	'font.size': 12,
	'axes.grid': True,
	'font.family': 'serif',
    'mathtext.fontset': 'cm'
}
)

# sample on ploting a simple line graph
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x+np.pi/4)
fig, ax = plt.subplots()
ax.plot(x, y1, label=r'$\sin(x)$', color='blue', linestyle='-', linewidth=2)
ax.plot(x, y2, label=r'$\cos(x + \pi/4)$', color='orange', linestyle='--', linewidth=2)
ax.set_title('Sine and Cosine Functions')
ax.set_xlabel('x values')
ax.set_ylabel('Function values')
plt.legend(frameon=False, loc='upper right')
plt.show()
plt.close()