"""
Aliased versus anti-aliased
=============================

This example demonstrates aliased versus anti-aliased text.
"""

import matplotlib.pyplot as plt

size = 128, 16
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi, layout="constrained")
fig.patch.set_alpha(0)

ax = fig.subplots()
ax.set_frame_on(False)

plt.rcParams["text.antialiased"] = True
ax.text(0.5, 0.5, "Anti-aliased", ha="center", va="center")

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
