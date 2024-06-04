"""
Marker size
===========

Demo the marker size control in matplotlib.
"""

import matplotlib.pyplot as plt

size = 256, 32
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig, ax = plt.subplots(figsize=figsize, dpi=dpi, layout="constrained")
fig.patch.set_alpha(0)
ax.set_frame_on(False)

for i in range(1, 11):
    ax.plot(
        [
            i,
        ],
        [
            1,
        ],
        "s",
        markersize=i,
        markerfacecolor="w",
        markeredgewidth=0.5,
        markeredgecolor="k",
    )

ax.set_xlim(0, 11)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
