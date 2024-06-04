"""
Dash join style
================

Example demoing the dash join style.
"""

import numpy as np
import matplotlib.pyplot as plt

size = 256, 64
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig, ax = plt.subplots(figsize=figsize, dpi=dpi, layout="constrained")
fig.patch.set_alpha(0)
ax.set_frame_on(False)

ax.plot(
    np.arange(3),
    [0, 1, 0],
    color="blue",
    dashes=[12, 5],
    linewidth=8,
    dash_joinstyle="miter",
)
ax.plot(
    4 + np.arange(3),
    [0, 1, 0],
    color="blue",
    dashes=[12, 5],
    linewidth=8,
    dash_joinstyle="bevel",
)
ax.plot(
    8 + np.arange(3),
    [0, 1, 0],
    color="blue",
    dashes=[12, 5],
    linewidth=8,
    dash_joinstyle="round",
)

ax.set_xlim(0, 12)
ax.set_ylim(-1, 2)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
