import numpy as np

# -----------------------------
# Step 1: Original vectors
# -----------------------------
v1 = np.array([1, 2])
v2 = np.array([2, 1])

print("Original vectors:")
print("v1:", v1)
print("v2:", v2)

# -----------------------------
# Step 2: Transformation matrix
# -----------------------------
A = np.array([[2, 1],
              [1, 2]])

print("\nTransformation matrix A:")
print(A)

# -----------------------------
# Step 3: Transform vectors
# -----------------------------
v1_transformed = np.dot(A, v1)
v2_transformed = np.dot(A, v2)

print("\nTransformed vectors:")
print("A · v1 =", v1_transformed)
print("A · v2 =", v2_transformed)

# -----------------------------
# Step 4: Normalize
# -----------------------------
def normalize(v):
    return v / np.linalg.norm(v)

v1_norm = normalize(v1_transformed)
v2_norm = normalize(v2_transformed)

print("\nNormalized vectors:")
print("v1_norm:", v1_norm)
print("v2_norm:", v2_norm)

# -----------------------------
# Step 5: Cosine similarity
# -----------------------------
cosine_similarity = np.dot(v1_norm, v2_norm)

print("\nCosine Similarity:", cosine_similarity)