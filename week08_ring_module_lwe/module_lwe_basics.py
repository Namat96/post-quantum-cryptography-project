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


def mv(A, s):
    out = []

    for row in A:
        total = np.zeros(n, dtype=int)

        for j in range(len(s)):
            total += mul(row[j], s[j])

        out.append(total % q)

    return out


A = [
    [np.array([1, 2, 0, 1]), np.array([3, 0, 1, 2])],
    [np.array([2, 1, 1, 0]), np.array([1, 2, 0, 1])]
]

s = [
    np.array([1, 0, -1, 1]),
    np.array([0, 1, 1, -1])
]

e = [
    np.array([1, 0, 0, -1]),
    np.array([0, -1, 1, 0])
]


As = mv(A, s)

b = []

for i in range(2):
    b.append((As[i] + e[i]) % q)


print("Module-LWE Basic Example")
print("------------------------")

print("A =")
for row in A:
    print(row)

print("\ns =")
for item in s:
    print(item)

print("\ne =")
for item in e:
    print(item)

print("\nA*s mod q =")
for item in As:
    print(item)

print("\nb = A*s + e mod q")
for item in b:
    print(item)

print("\nmodulus q =", q)