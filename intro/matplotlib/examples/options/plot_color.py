"""
The colors matplotlib line plots
==================================

An example demoing the various colors taken by matplotlib's plot.
"""

import matplotlib.pyplot as plt

size = 256, 16
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig, ax = plt.subplots(figsize=figsize, dpi=dpi, layout="constrained")
fig.patch.set_alpha(0)

ax.set_frame_on(False)

for i in range(1, 11):
    ax.plot([i, i], [0, 1], lw=1.5)

ax.set_xlim(0, 11)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
