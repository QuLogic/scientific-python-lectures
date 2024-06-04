"""
Bar plot advanced
==================

An more elaborate bar plot example
"""

import numpy as np
import matplotlib.pyplot as plt

n = 16
X = np.arange(n)
Y1 = (1 - X / n) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / n) * np.random.uniform(0.5, 1.0, n)

fig, ax = plt.subplots()

ax.bar(X, Y1, facecolor="#9999ff", edgecolor="white")
ax.bar(X, -Y2, facecolor="#ff9999", edgecolor="white")
ax.set(xlim=(-0.5, n), xticks=[])
ax.set(ylim=(-1, 1), yticks=[])


# Add a title and a box around it
from matplotlib.patches import FancyBboxPatch

ax.add_patch(
    FancyBboxPatch(
        (-0.05, 0.87),
        width=0.66,
        height=0.165,
        clip_on=False,
        boxstyle="square,pad=0",
        zorder=3,
        facecolor="white",
        alpha=1.0,
        transform=ax.transAxes,
    )
)

ax.text(
    -0.05,
    1.02,
    " Bar Plot:              plt.bar(...)\n",
    horizontalalignment="left",
    verticalalignment="top",
    size="xx-large",
    transform=ax.transAxes,
)

ax.text(
    -0.05,
    1.01,
    "\n\n   Make a bar plot with rectangles ",
    horizontalalignment="left",
    verticalalignment="top",
    size="large",
    transform=ax.transAxes,
)

plt.show()
