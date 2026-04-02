# Week 7 - Original basis vs reduced basis

import numpy as np

original_b1 = np.array([7, 2])
original_b2 = np.array([5, 3])

# Reduced basis obtained from lattice_reduction.py
reduced_b1 = np.array([2, -1])
reduced_b2 = np.array([3, 4])

print("Original Basis vs Reduced Basis")
print("--------------------------------")

print("Original basis:")
print("b1 =", original_b1)
print("b2 =", original_b2)

print("\nReduced basis:")
print("b1 =", reduced_b1)
print("b2 =", reduced_b2)

print("\nOriginal lengths:")
print("b1 =", np.linalg.norm(original_b1))
print("b2 =", np.linalg.norm(original_b2))

print("\nReduced lengths:")
print("b1 =", np.linalg.norm(reduced_b1))
print("b2 =", np.linalg.norm(reduced_b2))

print("\nDeterminants:")
original_det = np.linalg.det(np.array([original_b1, original_b2]))
reduced_det = np.linalg.det(np.array([reduced_b1, reduced_b2]))

print("Original =", original_det)
print("Reduced =", reduced_det)

print("\nThe reduced basis contains shorter vectors while preserving the lattice area.")