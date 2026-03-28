# Week 6 - Closest Vector Problem (CVP)
# Simple demonstration of finding the lattice vector
# closest to a target vector

import numpy as np

# Basis vectors
b1 = np.array([2, 1])
b2 = np.array([1, 2])

# Target vector
target = np.array([4, 3])

print("Closest Vector Problem (CVP)")
print("----------------------------")

best_vector = None
best_distance = float("inf")
best_x = 0
best_y = 0

# Search small integer combinations
for x in range(-5, 6):
    for y in range(-5, 6):
        lattice_vector = x * b1 + y * b2

        distance = np.linalg.norm(target - lattice_vector)

        if distance < best_distance:
            best_distance = distance
            best_vector = lattice_vector
            best_x = x
            best_y = y

print("Target vector:", target)
print("Closest lattice vector:", best_vector)
print("Distance:", best_distance)
print("Coefficients: x =", best_x, ", y =", best_y)