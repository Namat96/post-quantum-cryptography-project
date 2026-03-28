# Week 6 - Lattice Basics
# Basic lattice generation using basis vectors

import numpy as np

# Define two basis vectors
b1 = np.array([2, 1])
b2 = np.array([1, 2])

print("Basis vectors:")
print("b1 =", b1)
print("b2 =", b2)

# Generate lattice points
print("\nLattice points:")

for x in range(-3, 4):
    for y in range(-3, 4):
        point = x * b1 + y * b2
        print(f"({x}, {y}) -> {point}")