"""
Plotting a scatter of points
==============================

A simple example showing how to plot a scatter of points with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

n = 1024
rng = np.random.default_rng()
X = rng.normal(0, 1, n)
Y = rng.normal(0, 1, n)
T = np.arctan2(Y, X)

fig, ax = plt.subplots(layout="constrained")
ax.scatter(X, Y, s=75, c=T, alpha=0.5)

ax.set(xlim=(-1.5, 1.5), xticks=[])
ax.set(ylim=(-1.5, 1.5), yticks=[])

plt.show()
