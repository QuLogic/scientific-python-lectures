"""
Plotting a vector field: quiver
================================

A simple example showing how to plot a vector field (quiver) with
matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

n = 8
X, Y = np.mgrid[0:n, 0:n]
T = np.arctan2(Y - n / 2.0, X - n / 2.0)
R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
U, V = R * np.cos(T), R * np.sin(T)

fig, ax = plt.subplots(layout="constrained")
ax.quiver(X, Y, U, V, R, alpha=0.5)
ax.quiver(X, Y, U, V, edgecolor="k", facecolor="None", linewidth=0.5)

ax.set(xlim=(-1, n), xticks=[])
ax.set(ylim=(-1, n), yticks=[])

plt.show()
