# Polynomial Ring Experiment
# Week 5 - SageMath for Post-Quantum Cryptography

print("Polynomial Ring Experiment")

# Create polynomial ring over Z_23
R.<x> = PolynomialRing(Zmod(23))

# Define polynomials
f = x^2 + 3*x + 2
g = x^3 + 2*x + 5

print("\nPolynomial f:")
print(f)

print("\nPolynomial g:")
print(g)

# Addition
print("\nf + g:")
print(f + g)

# Multiplication
print("\nf * g:")
print(f * g)

# Evaluation
print("\nf(2):")
print(f(2))

# Polynomial degree
print("\nDegree of f:")
print(f.degree())

print("\nDegree of g:")
print(g.degree())

# Polynomial ring modulo x^4 + 1
S.<y> = PolynomialRing(Zmod(23))
modulus = y^4 + 1

print("\nPolynomial modulus:")
print(modulus)

print("\nPolynomial ring experiment completed.")
