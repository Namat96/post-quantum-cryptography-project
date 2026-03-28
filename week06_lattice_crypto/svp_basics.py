# Week 6 - Shortest Vector Problem (SVP)

import numpy as np

# Define lattice basis vectors
b1 = np.array([2, 1])
b2 = np.array([1, 2])

# Generate lattice vectors
vectors = []

for x in range(-3, 4):
    for y in range(-3, 4):
        if x == 0 and y == 0:
            continue

        vector = x * b1 + y * b2
        length = np.linalg.norm(vector)

        vectors.append((length, x, y, vector))

# Find the shortest non-zero vector
shortest = min(vectors, key=lambda item: item[0])

print("Shortest Vector Problem (SVP)")
print("--------------------------------")
print("Shortest vector:", shortest[3])
print("Length:", shortest[0])
print("Coefficients: x =", shortest[1], ", y =", shortest[2])