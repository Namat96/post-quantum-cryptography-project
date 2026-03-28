# Week 6 - Gram-Schmidt Orthogonalization

import numpy as np

print("Gram-Schmidt Orthogonalization")
print("--------------------------------")

# Original lattice basis vectors
b1 = np.array([2.0, 1.0])
b2 = np.array([1.0, 2.0])

# First orthogonal vector
u1 = b1

# Projection of b2 onto u1
projection = (np.dot(b2, u1) / np.dot(u1, u1)) * u1

# Second orthogonal vector
u2 = b2 - projection

print("Original basis:")
print("b1 =", b1)
print("b2 =", b2)

print("\nOrthogonal basis:")
print("u1 =", u1)
print("u2 =", u2)

print("\nDot product u1 · u2 =", np.dot(u1, u2))