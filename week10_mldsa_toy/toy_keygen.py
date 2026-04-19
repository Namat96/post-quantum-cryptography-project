import numpy as np

q = 17

# Small fixed values so the example gives the same result each time.
A = np.array([
    [2, 1],
    [3, 2]
])

s = np.array([2, 1])

# Public value t = A*s mod q
t = (A @ s) % q

print("Toy ML-DSA Key Generation")
print("-------------------------")
print("A =")
print(A)
print("secret s =", s)
print("public t =", t)
print("modulus q =", q)
print()
print("In a real ML-DSA scheme, the key generation process is much larger")
print("and uses polynomial matrices and carefully sampled values.")
