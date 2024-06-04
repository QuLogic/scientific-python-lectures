"""
A simple, good-looking plot
===========================

Demoing some simple features of matplotlib
"""

import numpy as np
import matplotlib

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 4), dpi=72, layout="constrained")
X = np.linspace(0, 2, 200)
Y = np.sin(2 * np.pi * X)
ax.plot(X, Y, lw=2)
ax.set_ylim(-1.1, 1.1)
ax.grid()

plt.show()
