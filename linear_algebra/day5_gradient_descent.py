import numpy as np

# Data
x = 2
y_true = 8

# Initialize weight
w = 1.0

# Learning rate
lr = 0.1

# Training loop
for i in range(10):
    # Prediction
    y_pred = w * x
    
    # Loss (MSE)
    loss = (y_pred - y_true) ** 2
    
    # Derivative of loss w.r.t w
    grad = 2 * (y_pred - y_true) * x
    
    # Update weight
    w = w - lr * grad
    
    print(f"Step {i+1}: w={w:.4f}, loss={loss:.4f}")

print("\nFinal weight:", w)