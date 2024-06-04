"""
Exercise
=========

Exercises with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5), dpi=80)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

ax.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
ax.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")

ax.spines[["right", "top"]].set_visible(False)
ax.spines[["left", "bottom"]].set_position("zero")

ax.set_xlim(X.min() * 1.1, X.max() * 1.1)
ax.set_xticks(
    [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
    [r"$-\pi$", r"$-\pi/2$", r"$0$", r"$+\pi/2$", r"$+\pi$"],
)

ax.set_ylim(C.min() * 1.1, C.max() * 1.1)
ax.set_yticks([-1, 1], [r"$-1$", r"$+1$"])

ax.legend(loc="upper left")

t = 2 * np.pi / 3
ax.plot([t, t], [0, np.cos(t)], color="blue", linewidth=1.5, linestyle="--")
ax.scatter(
    [
        t,
    ],
    [
        np.cos(t),
    ],
    50,
    color="blue",
)
ax.annotate(
    r"$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$",
    xy=(t, np.sin(t)),
    xycoords="data",
    xytext=(10, 30),
    textcoords="offset points",
    fontsize=16,
    arrowprops={"arrowstyle": "->", "connectionstyle": "arc3,rad=.2"},
)

ax.plot([t, t], [0, np.sin(t)], color="red", linewidth=1.5, linestyle="--")
ax.scatter(
    [
        t,
    ],
    [
        np.sin(t),
    ],
    50,
    color="red",
)
ax.annotate(
    r"$cos(\frac{2\pi}{3})=-\frac{1}{2}$",
    xy=(t, np.cos(t)),
    xycoords="data",
    xytext=(-90, -50),
    textcoords="offset points",
    fontsize=16,
    arrowprops={"arrowstyle": "->", "connectionstyle": "arc3,rad=.2"},
)

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox({"facecolor": "white", "edgecolor": "None", "alpha": 0.65})

plt.show()
