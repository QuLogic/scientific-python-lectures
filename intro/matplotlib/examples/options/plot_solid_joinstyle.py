"""
Solid joint style
==================

An example showing the different solid joint styles in matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

size = 256, 64
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig, ax = plt.subplots(figsize=figsize, dpi=dpi, layout="constrained")
fig.patch.set_alpha(0)
ax.set_frame_on(False)

ax.plot(np.arange(3), [0, 1, 0], color="blue", linewidth=8, solid_joinstyle="miter")
ax.plot(4 + np.arange(3), [0, 1, 0], color="blue", linewidth=8, solid_joinstyle="bevel")
ax.plot(8 + np.arange(3), [0, 1, 0], color="blue", linewidth=8, solid_joinstyle="round")

ax.set_xlim(0, 12)
ax.set_ylim(-1, 2)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
