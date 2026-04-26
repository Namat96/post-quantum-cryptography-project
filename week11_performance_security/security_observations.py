print("Week 11 - Security Observations")
print("--------------------------------")

points = [
    "Lattice based schemes are designed around hard mathematical problems.",
    "Security depends on the chosen parameters.",
    "Noise helps hide secret information in LWE style constructions.",
    "Poor parameter choices can make attacks easier.",
    "Toy examples are useful for learning but do not provide real cryptographic security.",
    "Real implementations also need protection against side-channel attacks."
]

for number, point in enumerate(points, 1):
    print(number, ".", point)

print()
print("Conclusion: security depends on mathematics, parameters and implementation.")
