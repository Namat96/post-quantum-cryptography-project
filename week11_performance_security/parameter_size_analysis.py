print("Week 11 - Toy Parameter Size Analysis")
print("--------------------------------------")

toy_kyber = {
    "public_vector": 4,
    "secret_vector": 4,
    "ciphertext_vector": 4
}

toy_mldsa = {
    "public_vector": 4,
    "secret_vector": 4,
    "signature_vector": 8
}

print("Toy ML-KEM / Kyber data:")
for name, size in toy_kyber.items():
    print(name, "coefficients =", size)

print()
print("Toy ML-DSA / Dilithium data:")
for name, size in toy_mldsa.items():
    print(name, "coefficients =", size)

print()
print("These are coefficient counts, not real standard key or signature sizes.")
