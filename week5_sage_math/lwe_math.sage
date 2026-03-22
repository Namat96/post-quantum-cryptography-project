# LWE Mathematical Experiment
# Week 5 - SageMath for Post-Quantum Cryptography

print("LWE Mathematical Experiment")

# Parameters
n = 4
q = 23

# Secret vector
s = vector(Zmod(q), [3, 7, 11, 5])

# Public matrix
A = matrix(Zmod(q), [
    [2, 4, 7, 9],
    [1, 6, 3, 8],
    [5, 2, 10, 4],
    [7, 9, 1, 6]
])

# Small error vector
e = vector(Zmod(q), [1, 0, -1, 1])

# LWE-style computation
b = A * s + e

print("\nParameters")
print("Dimension n =", n)
print("Modulus q =", q)

print("\nSecret vector s:")
print(s)

print("\nPublic matrix A:")
print(A)

print("\nError vector e:")
print(e)

print("\nLWE-style public vector b = A*s + e:")
print(b)

# Verify the relationship
print("\nVerification:")
print("A*s + e =", A * s + e)
print("b =", b)

if b == A * s + e:
    print("LWE relation verified successfully.")
