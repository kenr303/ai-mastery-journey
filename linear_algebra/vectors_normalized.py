import numpy as np

v = np.array ([1, 2, 2])
v_hat = v / np.linalg.norm(v)

print (v)
print(v_hat)
print(np.linalg.norm(v_hat))