import hashlib
import numpy as np

q = 17

A = np.array([
    [2, 1],
    [3, 2]
])

s = np.array([2, 1])
t = (A @ s) % q

message = "Post-quantum cryptography"

# Signature values produced by toy_sign.py.
z = np.array([12, 16])

def challenge(value, text):
    data = bytes(int(x) % 256 for x in value) + text.encode()
    return int.from_bytes(hashlib.sha256(data).digest(), "big") % q

# Recover the committed value from the public key and signature.
# c = 14 for this fixed toy message and commitment.
c = 14
w_check = (A @ z - c * t) % q
c_check = challenge(w_check, message)

print("Toy ML-DSA Verification")
print("-----------------------")
print("message =", message)
print("public t =", t)
print("signature z =", z)
print("recovered w =", w_check)
print("challenge =", c_check)

if c_check == c:
    print("signature valid")
else:
    print("signature invalid")

print()
print("Real ML-DSA verification includes additional checks and parameters.")
