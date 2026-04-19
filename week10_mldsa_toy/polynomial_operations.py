import numpy as np

q = 17
n = 4

def poly_add(a, b):
    return (np.array(a) + np.array(b)) % q

def poly_mul(a, b):
    t = np.convolve(a, b)
    r = np.zeros(n, dtype=int)

    for d, value in enumerate(t):
        if d < n:
            r[d] += value
        else:
            r[d - n] -= value

    return r % q

a = np.array([1, 2, 1, 0])
b = np.array([2, 0, 1, 1])

print("Toy Polynomial Operations")
print("-------------------------")
print("a =", a)
print("b =", b)
print("a + b mod q =", poly_add(a, b))
print("a * b mod (x^n + 1, q) =", poly_mul(a, b))
print("q =", q)
