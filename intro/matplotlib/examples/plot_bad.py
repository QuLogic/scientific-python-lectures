"""
A simple plotting example
==========================

A plotting example which can be improved with a few simple tweaks
"""

import numpy as np

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 4), dpi=72, layout="constrained")
x = np.linspace(0, 2, 200)
y = np.sin(2 * np.pi * x)
ax.plot(x, y, lw=0.25, c="k")
ax.set_xticks(np.arange(0.0, 2.0, 0.1))
ax.set_yticks(np.arange(-1.0, 1.0, 0.1))
ax.grid()
plt.show()
