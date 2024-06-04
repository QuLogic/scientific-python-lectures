"""
Subplot grid
=============

An example showing the subplot grid in matplotlib.
"""

import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(6, 4), layout="constrained")

for i, ax_row in enumerate(axs):
    for j, ax in enumerate(ax_row):
        ax.text(
            0.5, 0.5, f"axs[{i}][{j}]", ha="center", va="center", size=20, alpha=0.5
        )
        ax.set(xticks=[], yticks=[])

plt.show()
