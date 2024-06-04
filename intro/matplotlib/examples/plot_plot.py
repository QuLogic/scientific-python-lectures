"""
Plot and filled plots
=====================

Simple example of plots and filling between them with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi, np.pi, n)
Y = np.sin(2 * X)

fig, ax = plt.subplots(layout="constrained")

ax.plot(X, Y + 1, color="blue", alpha=1.00)
ax.fill_between(X, 1, Y + 1, color="blue", alpha=0.25)

ax.plot(X, Y - 1, color="blue", alpha=1.00)
ax.fill_between(X, -1, Y - 1, (Y - 1) > -1, color="blue", alpha=0.25)
ax.fill_between(X, -1, Y - 1, (Y - 1) < -1, color="red", alpha=0.25)

ax.set(xlim=(-np.pi, np.pi), xticks=[])
ax.set(ylim=(-2.5, 2.5), yticks=[])

plt.show()
