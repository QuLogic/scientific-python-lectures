"""
Colormaps
=========

An example plotting the matplotlib colormaps.
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.outer(np.arange(0, 1, 0.01), np.ones(2))

maps = [m for m in plt.colormaps if not m.endswith("_r")]
maps.sort()

fig, axs = plt.subplots(2, int(np.ceil(len(maps)/2)), figsize=(10, 5), layout="constrained")

for ax, cmap in zip(axs.flat, maps):
    ax.axis("off")
    ax.imshow(a, aspect="auto", cmap=cmap, origin="lower")
    ax.set_title(cmap, rotation=90, fontsize=10, va="bottom")

# ensure empty space has no axes if number of cmaps is odd
axs.flat[-1].axis("off")

plt.show()
