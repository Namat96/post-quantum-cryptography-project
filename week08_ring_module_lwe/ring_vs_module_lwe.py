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


# Ring-LWE example
a = np.array([1, 2, 3, 1])
s = np.array([1, -1, 0, 1])
e = np.array([1, 0, -1, 0])

ring_b = (mul(a, s) + e) % q

# Module-LWE style example
A = np.array([
    [1, 2, 3, 1],
    [2, 1, 1, 3]
])

s_module = np.array([
    [1, 0, 1, -1],
    [0, 1, -1, 1]
])

e_module = np.array([
    [1, 0, -1, 0],
    [0, 1, 0, -1]
])

module_b = []

for i in range(len(A)):
    value = (A[i] + s_module[i] + e_module[i]) % q
    module_b.append(value)


print("Ring-LWE vs Module-LWE")
print("----------------------")

print("Ring-LWE:")
print("a =", a)
print("s =", s)
print("e =", e)
print("b =", ring_b)

print("\nModule-LWE:")
print("A =")
print(A)
print("s =")
print(s_module)
print("e =")
print(e_module)
print("b =")
print(np.array(module_b))

print("\nmodulus q =", q)