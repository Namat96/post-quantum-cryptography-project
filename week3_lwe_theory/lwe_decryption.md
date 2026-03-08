# LWE Decryption

To decrypt the ciphertext, the receiver uses the secret key s.

Ciphertext:
(c1 , c2)

Where:

c1 = A^T * r  
c2 = b^T * r + m

Decryption step:

Compute:

m' = c2 - s^T * c1

Substitute:

b = A*s + e

We get:

m' = m + small error

Since the error term is small,
the original message m can be recovered.

Explanation:

The secret vector s cancels the main term
from the encryption equation.

Only a small noise remains,
which can be removed during decoding.a
