# Week 7 - Gram-Schmidt reduction
# A simple example using a two-dimensional lattice basis.

import numpy as np

b1 = np.array([4.0, 1.0])
b2 = np.array([3.0, 2.0])

u1 = b1
projection = (np.dot(b2, u1) / np.dot(u1, u1)) * u1
u2 = b2 - projection

print("Gram-Schmidt Orthogonalization")
print("------------------------------")
print("Original basis:")
print("b1 =", b1)
print("b2 =", b2)

print("\nOrthogonal vectors:")
print("u1 =", u1)
print("u2 =", u2)

print("\nDot product:")
print("u1 · u2 =", np.dot(u1, u2))
