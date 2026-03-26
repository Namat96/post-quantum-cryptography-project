# Ring-LWE Mathematical Experiment
# Week 5 - SageMath for Post-Quantum Cryptography

print("Ring-LWE Mathematical Experiment")

# Parameters
q = 23
n = 4

# Polynomial ring modulo q
R.<x> = PolynomialRing(Zmod(q))

# Quotient ring R_q = Z_q[x] / (x^n + 1)
S.<y> = R.quotient(x^n + 1)

print("\nModulus q:")
print(q)

print("\nPolynomial degree n:")
print(n)

print("\nQuotient ring:")
print(S)

# Secret polynomial
s = S(1 + 2*y + y^2)

# Public polynomial
a = S(3 + y + 4*y^2 + 2*y^3)

# Small error polynomial
e = S(1 - y)

# Ring-LWE style computation
b = a * s + e

print("\nSecret polynomial s:")
print(s)

print("\nPublic polynomial a:")
print(a)

print("\nError polynomial e:")
print(e)

print("\nRing-LWE public polynomial b = a*s + e:")
print(b)

# Verify relation
print("\nVerification:")
print("a*s + e =", a*s + e)
print("b =", b)

if b == a*s + e:
    print("Ring-LWE relation verified successfully.")

print("\nRing-LWE mathematical experiment completed.")
