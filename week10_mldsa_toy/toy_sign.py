import hashlib
import numpy as np

q = 17

A = np.array([
    [2, 1],
    [3, 2]
])

s = np.array([2, 1])

message = "Post-quantum cryptography"

# Small fixed masking vector for this toy example.
y = np.array([1, 2])

def challenge(value, text):
    data = bytes(int(x) % 256 for x in value) + text.encode()
    return int.from_bytes(hashlib.sha256(data).digest(), "big") % q

# Commit first, then derive a small challenge.
w = (A @ y) % q
c = challenge(w, message)

# Toy response.
z = (y + c * s) % q

print("Toy ML-DSA Signing")
print("------------------")
print("message =", message)
print("y =", y)
print("w =", w)
print("challenge c =", c)
print("signature z =", z)
print("modulus q =", q)
print()
print("This is a simplified learning example, not real ML-DSA signing.")
