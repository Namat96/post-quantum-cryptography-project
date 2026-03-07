# LWE Key Generation

In an LWE-based cryptosystem, keys are generated using the LWE equation.

Let:

q = modulus  
n = dimension  

Steps:

1. Generate a random matrix:

A ∈ Z_q^{m×n}

2. Choose a secret vector:

s ∈ Z_q^n

3. Generate a small error vector:

e ∈ Z_q^m

4. Compute:

b = A*s + e (mod q)

Public Key:
(A , b)

Private Key:
s

Explanation:

The matrix A and vector b are public.

However, recovering the secret vector s from
(A , b) is difficult because of the noise term e.

This hardness is based on the Learning With Errors problem.
