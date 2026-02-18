# Day 2 - Matrix Operations
# Author: Namat

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix addition
C = A + B

# Matrix multiplication
D = A @ B

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A + B:\n", C)
print("A x B:\n", D)
