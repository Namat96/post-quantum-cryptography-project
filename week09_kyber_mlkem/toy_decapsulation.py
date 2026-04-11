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


# Toy values from the previous experiments
s = np.array([1, -1, 0, 1])
u = np.array([4, 8, 13, 7])

shared_value = poly_mul(u, s)

print("Toy Kyber Decapsulation")
print("-----------------------")
print("secret s =", s)
print("ciphertext component u =", u)
print("u * s mod (x^n + 1, q) =", shared_value)
print("In real ML-KEM, decapsulation also performs message recovery and ciphertext checks.")
