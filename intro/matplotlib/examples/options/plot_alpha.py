"""
Alpha: transparency
===================

This example demonstrates using alpha for transparency.
"""

import matplotlib.pyplot as plt

size = 256, 16
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig, ax = plt.subplots(figsize=figsize, layout="constrained")
fig.patch.set_alpha(0)
ax.set_frame_on(False)

for i in range(1, 11):
    ax.axvline(i, linewidth=1, color="blue", alpha=0.25 + 0.75 * i / 10.0)

ax.set_xlim(0, 11)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
