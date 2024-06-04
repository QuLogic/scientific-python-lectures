"""
Plotting in polar coordinates
=============================

A simple example showing how to plot in polar coordinates with
matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


N = 20
theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
rng = np.random.default_rng()
radii = 10 * rng.random(N)
width = np.pi / 4 * rng.random(N)

fig = plt.figure(layout="constrained")
ax = fig.add_subplot(polar=True)

bars = ax.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars, strict=True):
    bar.set_facecolor(plt.cm.viridis(r / 10.0))
    bar.set_alpha(0.5)

ax.set(xticklabels=[], yticklabels=[])
plt.show()
