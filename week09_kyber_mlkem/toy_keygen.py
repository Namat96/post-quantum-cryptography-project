import numpy as np

q = 17
n = 4


def poly_mul(a, b):
    """Multiply polynomials modulo x^n + 1 and q."""
    t = np.convolve(a, b)
    r = np.zeros(n, dtype=int)

    for d, value in enumerate(t):
        if d < n:
            r[d] += value
        else:
            r[d - n] -= value

    return r % q


A = np.array([1, 2, 3, 1])
s = np.array([1, -1, 0, 1])
e = np.array([1, 0, -1, 0])

# b = A*s + e (mod q)
b = (poly_mul(A, s) + e) % q

print("Toy Kyber Key Generation")
print("-------------------------")
print("A =", A)
print("s =", s)
print("e =", e)
print("public component b =", b)
print("secret component s =", s % q)
print("modulus q =", q)
