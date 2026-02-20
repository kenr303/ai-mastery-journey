def dot_product (v1, v2):
    if len(v1) != len(v2):
        raise ValueError ("Vectors must be the same length")
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total

a = [2, 3]
b = [-3, -5]
print("Dot Product:", dot_product (a, b))