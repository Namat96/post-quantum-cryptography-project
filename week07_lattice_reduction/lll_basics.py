# Week 7 - Basic LLL idea
# This small example shows the size-reduction step used in LLL.

import numpy as np

b1 = np.array([4, 1], dtype=float)
b2 = np.array([3, 2], dtype=float)

mu = round(np.dot(b2, b1) / np.dot(b1, b1))
reduced_b2 = b2 - mu * b1

print("Basic LLL Size Reduction")
print("-------------------------")
print("Original basis:")
print("b1 =", b1)
print("b2 =", b2)

print("\nmu =", mu)
print("Reduced second vector =", reduced_b2)

print("\nLength of original b2 =", np.linalg.norm(b2))
print("Length of reduced b2 =", np.linalg.norm(reduced_b2))
