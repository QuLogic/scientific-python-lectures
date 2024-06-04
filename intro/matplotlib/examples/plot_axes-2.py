"""
Axes
====

This example shows various axes command to position matplotlib axes.

"""

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.5, 0.5])
ax.set(xticks=[], yticks=[])
ax.text(
    0.5, 0.1, "add_axes([0.1, 0.1, 0.5, 0.5])", ha="center", va="center", size=16, alpha=0.5
)

ax = fig.add_axes([0.2, 0.2, 0.5, 0.5])
ax.set(xticks=[], yticks=[])
ax.text(
    0.5, 0.1, "add_axes([0.2, 0.2, 0.5, 0.5])", ha="center", va="center", size=16, alpha=0.5
)

ax = fig.add_axes([0.3, 0.3, 0.5, 0.5])
ax.set(xticks=[], yticks=[])
ax.text(
    0.5, 0.1, "add_axes([0.3, 0.3, 0.5, 0.5])", ha="center", va="center", size=16, alpha=0.5
)

ax = fig.add_axes([0.4, 0.4, 0.5, 0.5])
ax.set(xticks=[], yticks=[])
ax.text(
    0.5, 0.1, "add_axes([0.4, 0.4, 0.5, 0.5])", ha="center", va="center", size=16, alpha=0.5
)

plt.show()
