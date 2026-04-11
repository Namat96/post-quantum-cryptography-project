import numpy as np

q = 17
samples = np.array([-2, -1, 0, 1, 2])

print("Noise Experiment")
print("----------------")
print("modulus q =", q)
print("small noise values =", samples)
print()

for value in samples:
    reduced = value % q
    print(f"noise {value:2d} -> modulo q: {reduced:2d}")

print()
print("Small noise is important in lattice-based schemes because it hides the secret")
print("while keeping the intended computation recoverable.")
