"""
3D plotting
===========

A simple example of 3D plotting.
"""

import numpy as np
import matplotlib.pyplot as plt


X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap=plt.cm.hot)
ax.set_zlim(-2, 2)

plt.show()
