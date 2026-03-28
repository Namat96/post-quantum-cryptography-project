# Week 6 - Lattice Matrix Representation

import numpy as np

# Define lattice basis vectors
b1 = np.array([2, 1])
b2 = np.array([1, 2])

# Create basis matrix
B = np.column_stack((b1, b2))

print("Lattice basis matrix:")
print(B)

print("\nDeterminant:")
print(np.linalg.det(B))

print("\nBasis vectors:")
print("b1 =", b1)
print("b2 =", b2)