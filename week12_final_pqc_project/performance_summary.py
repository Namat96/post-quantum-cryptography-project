print("Performance and Security Summary")
print("---------------------------------")

tests = [
    ("Lattice calculations", "small integer examples"),
    ("LWE", "small vectors and noise"),
    ("ML-KEM", "polynomial and matrix operations"),
    ("ML-DSA", "signature operations")
]

for name, detail in tests:
    print(name, "->", detail)

print()
print("My main observation is that the small examples run quickly.")
print("Real post-quantum cryptographic systems use much larger")
print("parameters and more complicated operations.")
print()
print("So both security and performance are important when")
print("working with practical post-quantum cryptography.")
