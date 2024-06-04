"""
Pie chart
=========

A simple pie chart example with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

n = 20
Z = np.ones(n)
Z[-1] *= 2

fig, ax = plt.subplots(layout="constrained")

ax.pie(Z, explode=Z * 0.05, colors=[f"{i / float(n):f}" for i in range(n)])
ax.axis("equal")
ax.set_xticks([])
ax.set_yticks([])

plt.show()
