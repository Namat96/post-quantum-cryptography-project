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


# Small Ring-LWE sampling example
a = np.array([1, 2, 3, 1])
s = np.array([1, -1, 0, 1])
e = np.array([1, 0, -1, 0])

p = (mul(a, s) + e) % q

print("Ring-LWE Sampling Example")
print("-------------------------")
print("a =", a)
print("s =", s)
print("e =", e)
print("p =", p)
print("modulus q =", q)