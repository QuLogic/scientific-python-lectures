"""
Dash capstyle
=============

An example demoing the dash capstyle.
"""

import numpy as np
import matplotlib.pyplot as plt

size = 256, 16
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig, ax = plt.subplots(figsize=figsize, dpi=dpi, layout="constrained")
fig.patch.set_alpha(0)
ax.set_frame_on(False)

ax.plot(
    np.arange(4),
    np.ones(4),
    color="blue",
    dashes=[15, 15],
    linewidth=8,
    dash_capstyle="butt",
)

ax.plot(
    5 + np.arange(4),
    np.ones(4),
    color="blue",
    dashes=[15, 15],
    linewidth=8,
    dash_capstyle="round",
)

ax.plot(
    10 + np.arange(4),
    np.ones(4),
    color="blue",
    dashes=[15, 15],
    linewidth=8,
    dash_capstyle="projecting",
)

ax.set_xlim(0, 14)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
