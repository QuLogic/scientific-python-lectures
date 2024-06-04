"""
Linestyles
==========

Plot the different line styles.
"""

import numpy as np
import matplotlib.pyplot as plt


def linestyle(ax, ls, i):
    X = i * 0.5 * np.ones(11)
    Y = np.arange(11)
    ax.plot(
        X,
        Y,
        ls,
        color=(0.0, 0.0, 1, 1),
        lw=3,
        ms=8,
        mfc=(0.75, 0.75, 1, 1),
        mec=(0, 0, 1, 1),
    )
    ax.text(0.5 * i, 10.25, ls, rotation=90, fontsize=15, va="bottom")


linestyles = [
    "-",
    "--",
    ":",
    "-.",
    ".",
    ",",
    "o",
    "^",
    "v",
    "<",
    ">",
    "s",
    "+",
    "x",
    "d",
    "1",
    "2",
    "3",
    "4",
    "h",
    "p",
    "|",
    "_",
    "D",
    "H",
]
n_lines = len(linestyles)

size = 20 * n_lines, 300
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig, ax = plt.subplots(figsize=figsize, dpi=dpi, layout="constrained")
ax.set_frame_on(False)

for i, ls in enumerate(linestyles):
    linestyle(ax, ls, i)

ax.set_xlim(-0.2, 0.2 + 0.5 * n_lines)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
