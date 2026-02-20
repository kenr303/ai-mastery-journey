def dot_product (v1, v2):
    if len(v1) != len(v2):
        raise ValueError ("Vectors must be the same length")
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total

a = [1, 2, 3]
b = [4, 5, 6]
print("Dot Product:", dot_product (a, b))