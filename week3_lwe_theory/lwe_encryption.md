# LWE Encryption

In an LWE cryptosystem, encryption uses the public key (A, b).

Public key:
(A, b)

Private key:
s

Where:

b = A*s + e (mod q)

Encryption steps:

1. Choose a random vector:

r ∈ {0,1}^m

2. Compute:

c1 = A^T * r

3. Compute:

c2 = b^T * r + m

Ciphertext:

(c1 , c2)

Explanation:

The random vector r ensures that encryption is probabilistic.

Even if the same message is encrypted multiple times,
the ciphertext will be different.

This property is important for security.
