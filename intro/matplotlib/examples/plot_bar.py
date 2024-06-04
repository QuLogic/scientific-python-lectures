"""
Bar plots
==========

An example of bar plots with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)
rng = np.random.default_rng()
Y1 = (1 - X / float(n)) * rng.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * rng.uniform(0.5, 1.0, n)

fig, ax = plt.subplots(layout="constrained")
ax.bar(X, +Y1, facecolor="#9999ff", edgecolor="white")
ax.bar(X, -Y2, facecolor="#ff9999", edgecolor="white")

for x, y in zip(X, Y1, strict=True):
    ax.text(x + 0.4, y + 0.05, f"{y:.2f}", ha="center", va="bottom")

for x, y in zip(X, Y2, strict=True):
    ax.text(x + 0.4, -y - 0.05, f"{y:.2f}", ha="center", va="top")

ax.set(xlim=(-0.5, n), xticks=[])
ax.set(ylim=(-1.25, 1.25), yticks=[])

plt.show()
