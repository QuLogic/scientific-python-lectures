"""
Horizontal arrangement of subplots
==================================

An example showing horizontal arrangement of subplots with matplotlib.
"""

import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(6, 4), layout="constrained")

for i, ax in enumerate(axs):
    ax.text(0.5, 0.5, f"subplot(2,1,{i})", ha="center", va="center", size=24, alpha=0.5)
    ax.set(xticks=[], yticks=[])

plt.show()
