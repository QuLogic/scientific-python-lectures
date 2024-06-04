"""
Exercise 2
===========

Exercise 2 with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a new figure of size 8x6 inches, using 100 dots per inch with one Axes
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plot cosine using blue color with a continuous line of width 1 point
ax.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Plot sine using green color with a continuous line of width 1 point
ax.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Set x limits
ax.set_xlim(-4.0, 4.0)

# Set x ticks
ax.set_xticks(np.linspace(-4, 4, 9))

# Set y limits
ax.set_ylim(-1.0, 1.0)

# Set y ticks
ax.set_yticks(np.linspace(-1, 1, 5))

# Show result on screen
plt.show()
