"""
Imshow elaborate
=================

An example demoing imshow and styling the figure.
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2) - y**2)


n = 10
x = np.linspace(-3, 3, int(3.5 * n))
y = np.linspace(-3, 3, int(3.0 * n))
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig, ax = plt.subplots(layout="constrained")
im = ax.imshow(Z, interpolation="nearest", cmap="bone", origin="lower")
fig.colorbar(im, ax=ax, shrink=0.92)

ax.set_xticks([])
ax.set_yticks([])
plt.show()
