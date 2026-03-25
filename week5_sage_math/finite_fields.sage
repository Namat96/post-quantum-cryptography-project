# Finite Fields Experiment
# Week 5 - SageMath for Post-Quantum Cryptography

print("Finite Fields Experiment")

# Create the finite field GF(7)
F = GF(7)

print("\nFinite field:")
print(F)

# Elements of the field
a = F(3)
b = F(5)

print("\nElement a =", a)
print("Element b =", b)

# Field operations
print("\na + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

# Powers
print("\na^2 =", a^2)
print("a^3 =", a^3)

# Multiplicative inverse
print("\nInverse of a:")
print(a.inverse_of_unit())

# Create a larger finite field
K.<z> = GF(2^4)

print("\nFinite field GF(2^4):")
print(K)

print("\nGenerator:")
print(z)

print("\nFinite field experiment completed.")
