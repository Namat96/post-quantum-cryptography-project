import numpy as np

q = 17
n = 4


def poly_mul(a, b):
    t = np.convolve(a, b)
    r = np.zeros(n, dtype=int)

    for d, value in enumerate(t):
        if d < n:
            r[d] += value
        else:
            r[d - n] -= value

    return r % q


# Toy public key values
A = np.array([1, 2, 3, 1])
b = np.array([4, 4, 3, 2])

# Small random-looking ephemeral values
r = np.array([1, 0, -1, 1])
e1 = np.array([0, 1, 0, -1])

u = (poly_mul(A, r) + e1) % q

print("Toy Kyber Encapsulation")
print("-----------------------")
print("A =", A)
print("b =", b)
print("r =", r)
print("e1 =", e1)
print("ciphertext component u =", u)
print("modulus q =", q)
print("The real ML-KEM encapsulation uses matrices, noise sampling and a message encoding step.")
