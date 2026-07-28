import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': True,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting a simple 3d surface
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')  # 3d needs add_subplot, not plt.subplots
surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, antialiased=True)
fig.colorbar(surf, ax=ax, shrink=0.6, pad=0.12, label=r'$z$')

ax.set_title(r'$z = \sin(\sqrt{x^2 + y^2})$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(elev=30, azim=-60)  # camera angle
plt.show()
plt.close()
