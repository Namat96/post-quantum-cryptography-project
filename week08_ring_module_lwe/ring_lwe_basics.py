import numpy as np

q = 17
n = 4


def mul(a, b):
    t = np.convolve(a, b)
    r = np.zeros(n, dtype=int)

    for d, v in enumerate(t):
        if d < n:
            r[d] += v
        else:
            r[d - n] -= v

    return r % q


# Small Ring-LWE example
a = np.array([1, 2, 3, 1])
s = np.array([1, 0, 1, -1])
e = np.array([1, 0, -1, 1])

b = (mul(a, s) + e) % q

print("Ring-LWE Basic Example")
print("----------------------")
print("a =", a)
print("s =", s)
print("e =", e)
print("b =", b)
print("modulus q =", q)