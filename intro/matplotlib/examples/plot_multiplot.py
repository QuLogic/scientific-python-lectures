"""
Subplots
=========

Show multiple subplots in matplotlib.
"""

import matplotlib.pyplot as plt

fig = plt.figure()
fig.subplots_adjust(bottom=0.025, left=0.025, top=0.975, right=0.975)

ax = fig.add_subplot(2, 1, 1) 
ax.set_xticks([])
ax.set_yticks([])

ax = fig.add_subplot(2, 3, 4)
ax.set_xticks([])
ax.set_yticks([])

ax = fig.add_subplot(2, 3, 5)
ax.set_xticks([])
ax.set_yticks([])

ax = fig.add_subplot(2, 3, 6)
ax.set_xticks([])
ax.set_yticks([])


plt.show()
