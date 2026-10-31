# PythonMarg brings you
# Matplotlib project

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
u, v =np.meshgrid(u, v)
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_xlim(-20, 20); ax.set_ylim(-20, 20)
ax.set_zlim(-5, 5); ax.axis('off')

def animate(frame):
    ax.cla()
    scale = 1 + 0.1 *np.sin(np.radians(frame*6))
    x = scale * (16 * np.sin(u)**3)
    y = scale * (13 * np.cos(u) - 5*np.cos(2*u) - 2*np.cos(3*u) - np.cos(4*u))
    z = scale * (5 * np.sin(v))
    ax.plot_surface(x, y, z, color="white", edgecolor='r')
    ax.view_init(elev=30, azim=frame*2)
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_zlim(-5, 5)
    ax.axis('off')

ani = FuncAnimation(fig, animate, frames=360, interval=50)
plt.show()
