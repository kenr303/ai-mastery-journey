import numpy as np

# ----------------------------
# Generate simple dataset
# y = 3x1 + 2x2
# ----------------------------

X = np.array([
    [1, 2],
    [2, 1],
    [3, 1],
    [0, 2]
])

y = np.array([3*1 + 2*2,
              3*2 + 2*1,
              3*3 + 2*1,
              3*0 + 2*2])

# ----------------------------
# Initialize parameters
# ----------------------------

W = np.array([0.0, 0.0])
b = 0.0

lr = 0.01
epochs = 100

# ----------------------------
# Training loop
# ----------------------------

for epoch in range(epochs):

    total_loss = 0

    for i in range(len(X)):
        x1, x2 = X[i]
        y_true = y[i]

        # Prediction
        y_pred = W[0]*x1 + W[1]*x2 + b

        # Error
        error = y_pred - y_true

        # Loss
        loss = error**2
        total_loss += loss

        # Gradients
        dW1 = 2 * error * x1
        dW2 = 2 * error * x2
        db  = 2 * error

        # Update
        W[0] -= lr * dW1
        W[1] -= lr * dW2
        b    -= lr * db

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

print("\nLearned parameters:")
print("W:", W)
print("b:", b)