# Week 7 - Short vector search
# Search a small range of integer combinations of two basis vectors.

import numpy as np

b1 = np.array([4, 1])
b2 = np.array([1, 3])

shortest = None
shortest_coefficients = None
shortest_vector = None

for x in range(-5, 6):
    for y in range(-5, 6):
        if x == 0 and y == 0:
            continue

        vector = x * b1 + y * b2
        length = np.linalg.norm(vector)

        if shortest is None or length < shortest:
            shortest = length
            shortest_coefficients = (x, y)
            shortest_vector = vector

print("Short Vector Search")
print("-------------------")
print("Basis vectors:")
print("b1 =", b1)
print("b2 =", b2)

print("\nShortest vector found:")
print("Vector =", shortest_vector)
print("Coefficients =", shortest_coefficients)
print("Length =", shortest)
