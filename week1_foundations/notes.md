# Day 1 Notes – Modular Arithmetic

Modular arithmetic works with remainders.

(a + b) mod q  
(a × b) mod q  
a^e mod q  

Used in:
- RSA
- ECC
- LWE
- Ring-LWE

Why important:
All cryptographic algorithms rely on modular arithmetic.
# Day 2 Notes – Vectors & Matrices

Vectors are ordered lists of numbers.

Used in:
- LWE
- Ring-LWE
- Lattice cryptography

Matrices represent linear transformations.

Why important:
Post-quantum schemes rely on matrix and vector operations.
# Day 3 Notes – Number Theory Basics

GCD is used in key generation.

Extended Euclidean Algorithm computes modular inverse.

Modular inverse is required in:
- RSA
- ECC
- LWE

Prime numbers are fundamental in cryptography.

# Day 4 Notes – RSA

RSA Steps:
1. Choose primes p and q
2. Compute n = pq
3. Compute φ(n)
4. Choose e such that gcd(e, φ) = 1
5. Compute d = e^{-1} mod φ
6. Encrypt: c = m^e mod n
7. Decrypt: m = c^d mod n

RSA security relies on integer factorization.

