# Mathematical Definition of LWE

Let:

q = modulus  
n = dimension  

Choose:
A ∈ Z_q^{m×n}   (random matrix)
s ∈ Z_q^n       (secret vector)
e ∈ Z_q^m       (small error vector)

Compute:

b = A*s + e (mod q)

The Learning With Errors problem:

Given (A, b),
recover the secret vector s.

Why is this hard?

Because the error term e hides the linear relationship
between A and s.

Without noise (e = 0),
the system could be solved using linear algebra.

With noise,
recovering s becomes computationally difficult.
