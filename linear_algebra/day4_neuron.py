import numpy as np

# -------------------------
# Input vector (features)
# -------------------------
x = np.array([1.0, 2.0])

# -------------------------
# Weights
# -------------------------
W = np.array([0.5, -1.0])

# -------------------------
# Bias
# -------------------------
b = 0.5

# -------------------------
# Weighted sum
# -------------------------
z = np.dot(W, x) + b

print("Weighted sum (z):", z)

# -------------------------
# Activation functions
# -------------------------

def relu(z):
    return max(0, z)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

print("ReLU output:", relu(z))
print("Sigmoid output:", sigmoid(z))