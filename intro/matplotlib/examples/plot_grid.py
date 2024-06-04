"""
Grid
====

Displaying a grid on the axes in matploblib.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

fig, ax = plt.subplots(layout="constrained")

ax.set_xlim(0, 4)
ax.set_ylim(0, 3)

ax.xaxis.set_major_locator(mticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(mticker.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(mticker.MultipleLocator(0.1))

ax.grid(which="major", axis="x", linewidth=0.75, linestyle="-", color="0.75")
ax.grid(which="minor", axis="x", linewidth=0.25, linestyle="-", color="0.75")
ax.grid(which="major", axis="y", linewidth=0.75, linestyle="-", color="0.75")
ax.grid(which="minor", axis="y", linewidth=0.25, linestyle="-", color="0.75")

ax.set_xticklabels([])
ax.set_yticklabels([])

plt.show()
