"""
Exercise 3
==========

Exercise 3 with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5), dpi=100)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

ax.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
ax.plot(X, S, color="red", linewidth=2.5, linestyle="-")

ax.set_xlim(-4.0, 4.0)
ax.set_xticks(np.linspace(-4, 4, 9))

ax.set_ylim(-1.0, 1.0)
ax.set_yticks(np.linspace(-1, 1, 5))

plt.show()
