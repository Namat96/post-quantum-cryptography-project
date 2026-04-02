# Week 7 - Simple lattice basis reduction
# This is a small educational implementation for a 2D basis.

import numpy as np

def reduce_basis(b1, b2):
    b1 = np.array(b1, dtype=float)
    b2 = np.array(b2, dtype=float)

    changed = True

    while changed:
        changed = False

        if np.linalg.norm(b2) < np.linalg.norm(b1):
            b1, b2 = b2, b1
            changed = True

        mu = round(np.dot(b2, b1) / np.dot(b1, b1))

        if mu != 0:
            new_b2 = b2 - mu * b1
            if np.linalg.norm(new_b2) < np.linalg.norm(b2):
                b2 = new_b2
                changed = True

    return b1.astype(int), b2.astype(int)


b1 = [7, 2]
b2 = [5, 3]

print("Lattice Basis Reduction")
print("------------------------")
print("Original basis:")
print("b1 =", b1)
print("b2 =", b2)

r1, r2 = reduce_basis(b1, b2)

print("\nReduced basis:")
print("b1 =", r1)
print("b2 =", r2)

print("\nOriginal lengths:")
print("b1 =", np.linalg.norm(b1))
print("b2 =", np.linalg.norm(b2))

print("\nReduced lengths:")
print("b1 =", np.linalg.norm(r1))
print("b2 =", np.linalg.norm(r2))
