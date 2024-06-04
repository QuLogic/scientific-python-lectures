"""
Marker face color
==================

Demo the marker face color of matplotlib's markers.
"""

import numpy as np
import matplotlib.pyplot as plt

size = 256, 16
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig, ax = plt.subplots(figsize=figsize, dpi=dpi, layout="constrained")
fig.patch.set_alpha(0)
ax.set_frame_on(False)

rng = np.random.default_rng()

for i in range(1, 11):
    r, g, b = np.random.uniform(0, 1, 3)
    ax.plot(
        [
            i,
        ],
        [
            1,
        ],
        "s",
        markersize=8,
        markerfacecolor=(r, g, b, 1),
        markeredgewidth=0.1,
        markeredgecolor=(0, 0, 0, 0.5),
    )
ax.set_xlim(0, 11)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
