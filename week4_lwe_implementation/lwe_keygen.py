# LWE Key Generation
# Author: Namat

import numpy as np

q = 97
n = 4

# Generate random matrix A
A = np.random.randint(0, q, (n, n))

# Secret vector s
s = np.random.randint(0, q, (n, 1))

# Error vector e (small noise)
e = np.random.randint(-1, 2, (n, 1))

# Compute b = A*s + e mod q
b = (A @ s + e) % q

print("Public matrix A:\n", A)
print("Secret vector s:\n", s)
print("Error vector e:\n", e)
print("Vector b:\n", b)

print("\nPublic Key: (A, b)")
print("Private Key: s")
