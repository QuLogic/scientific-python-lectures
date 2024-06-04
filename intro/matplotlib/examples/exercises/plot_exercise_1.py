"""
Exercise 1
===========

Solution of the exercise 1 with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

fig, ax = plt.subplots()
ax.plot(X, C)
ax.plot(X, S)

plt.show()
