import math
def magnitude (v):
    total = 0
    for i in v:
        total = i**2
    return math.sqrt(total)

v = [3, 4]
print ("Vector:", v)
print ("Magnitude:", magnitude(v))