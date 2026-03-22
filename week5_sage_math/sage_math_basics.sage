# Week 5: SageMath Basics
# Post-Quantum Cryptography Project

print("SageMath Basics for Post-Quantum Cryptography")

# --------------------------------
# 1. Modular Arithmetic
# --------------------------------

a = 17
b = 23
p = 7

print("\nModular Arithmetic")
print("a + b mod p =", (a + b) % p)
print("a * b mod p =", (a * b) % p)

# --------------------------------
# 2. Vectors
# --------------------------------

print("\nVectors")

v = vector(ZZ, [1, 2, 3, 4])

print("Vector:", v)
print("Vector length:", v.norm())

# --------------------------------
# 3. Matrices
# --------------------------------

print("\nMatrices")

A = matrix(ZZ, [
    [1, 2],
    [3, 4]
])

print("Matrix:")
print(A)

print("Determinant:", A.det())

# --------------------------------
# 4. Polynomial Ring
# --------------------------------

print("\nPolynomial Ring")

R.<x> = PolynomialRing(ZZ)

f = x^2 + 3*x + 2

print("Polynomial:", f)
print("f(2) =", f(2))

# --------------------------------
# 5. Finite Field
# --------------------------------

print("\nFinite Field")

F = GF(7)

element = F(3)

print("Finite field:", F)
print("Element:", element)
print("Element squared:", element^2)

print("\nWeek 5 SageMath experiments completed.")
