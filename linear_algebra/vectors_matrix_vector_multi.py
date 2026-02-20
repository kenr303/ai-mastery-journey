import matplotlib.pyplot as plt
import numpy as np

v1 = np.array([2, 3])
v2 = np.array([4, 1])

plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')

plt.xlim(-1,5)
plt.ylim(-1,5)
plt.grid()
plt.legend()
plt.show()