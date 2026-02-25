# Grover’s Algorithm

Grover’s Algorithm is a quantum algorithm that speeds up
unstructured search problems.

Classical search complexity:
O(N)

Quantum search complexity:
O(√N)

Impact on Cryptography:

Symmetric cryptography (like AES) relies on brute-force resistance.

Example:
- AES-128 has 2^128 possible keys.
- With Grover’s algorithm, complexity becomes roughly 2^64.

This does NOT completely break symmetric cryptography,
but it reduces its security strength.

Mitigation:
- Double key sizes (e.g., use AES-256 instead of AES-128).

Conclusion:
Quantum computers weaken symmetric cryptography,
but do not destroy it like Shor’s algorithm does to RSA.
