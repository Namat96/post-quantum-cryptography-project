# Day 4 - Simple RSA Implementation
# Author: Nemat

import random

# Step 1: GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Step 2: Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# Step 3: Modular inverse
def mod_inverse(e, phi):
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        return None
    return x % phi

# Step 4: Choose small primes (demo only)
p = 11
q = 13

n = p * q
phi = (p - 1) * (q - 1)

# Step 5: Choose e
e = 7
while gcd(e, phi) != 1:
    e += 1

# Step 6: Compute d
d = mod_inverse(e, phi)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Step 7: Encrypt
message = 9
cipher = pow(message, e, n)
print("Encrypted:", cipher)

# Step 8: Decrypt
decrypted = pow(cipher, d, n)
print("Decrypted:", decrypted)
