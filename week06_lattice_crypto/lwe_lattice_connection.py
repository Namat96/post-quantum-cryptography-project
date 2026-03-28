# Week 6 - Connection Between LWE and Lattices
# Simple mathematical demonstration

import numpy as np

# Secret vector
s = np.array([2, 1])

# Public matrix
A = np.array([
    [1, 2],
    [3, 1]
])

# Small error vector
e = np.array([1, 0])

# LWE-style computation
b = A @ s + e

print("LWE and Lattice Connection")
print("--------------------------")

print("Secret vector s:", s)
print("Public matrix A:")
print(A)
print("Error vector e:", e)

print("\nComputed vector b = A*s + e:")
print(b)

print("\nWithout error A*s:")
print(A @ s)

print("\nThe small error makes it difficult to recover")
print("the secret vector s from A and b.")