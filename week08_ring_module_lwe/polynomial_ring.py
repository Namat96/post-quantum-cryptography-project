import numpy as np

q = 17
n = 4


def mul(a, b):
    # Polynomial multiplication
    t = np.convolve(a, b)

    # Result modulo x^n + 1
    r = np.zeros(n, dtype=int)

    for d, v in enumerate(t):
        if d < n:
            r[d] += v
        else:
            r[d - n] -= v

    return r % q


a = np.array([1, 2, 0, 1])
b = np.array([2, 1, 3, 0])

print("Polynomial Ring Example")
print("-----------------------")

print("a =", a)
print("b =", b)

result = mul(a, b)

print("a*b mod (x^n + 1) =", result)
print("modulus q =", q)