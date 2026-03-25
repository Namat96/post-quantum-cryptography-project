# Lattice Basics Experiment
# Week 5 - SageMath for Post-Quantum Cryptography

print("Lattice Basics Experiment")

# Create two-dimensional lattice basis vectors
B = matrix(ZZ, [
    [4, 1],
    [1, 3]
])

print("\nLattice basis matrix B:")
print(B)

# Basis vectors
b1 = vector(ZZ, [4, 1])
b2 = vector(ZZ, [1, 3])

print("\nBasis vector b1:")
print(b1)

print("\nBasis vector b2:")
print(b2)

# Determinant gives the area of the fundamental parallelogram
print("\nDeterminant of B:")
print(B.det())

# Generate a lattice point
v = vector(ZZ, [2, -1])

lattice_point = v[0] * b1 + v[1] * b2

print("\nInteger coefficients:")
print(v)

print("\nGenerated lattice point:")
print(lattice_point)

# Norm of the lattice point
print("\nEuclidean norm:")
print(lattice_point.norm())

print("\nLattice experiment completed.")
