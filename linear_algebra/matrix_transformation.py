import matplotlib.pyplot as plt
import numpy as np

# Original vectors
v1 = np.array([1,0])
v2 = np.array([0,1])

# Transformation matrix
A = np.array([[2,1],
              [1,2]])

# Transform vectors
v1_t = np.dot(A, v1)
v2_t = np.dot(A, v2)

# Plot original vectors
plt.quiver(0,0,v1[0],v1[1],color='r',angles='xy',scale_units='xy',scale=1,label='v1')
plt.quiver(0,0,v2[0],v2[1],color='b',angles='xy',scale_units='xy',scale=1,label='v2')

# Plot transformed vectors
plt.quiver(0,0,v1_t[0],v1_t[1],color='r',angles='xy',scale_units='xy',scale=1,linestyle='dashed',label='v1 transformed')
plt.quiver(0,0,v2_t[0],v2_t[1],color='b',angles='xy',scale_units='xy',scale=1,linestyle='dashed',label='v2 transformed')

plt.xlim(-1,5)
plt.ylim(-1,5)
plt.grid()
plt.legend()
plt.title("Matrix Transformation of 2D Vectors")
plt.show()