# Week 10 - Dilithium / ML-DSA

This week looks at lattice-based digital signatures and the basic idea behind
Dilithium, which is standardized as ML-DSA.

The programs here are small learning examples. They are not an implementation
of the real ML-DSA standard.

## Topics

- public and secret values in a lattice-based signature
- polynomial operations modulo q
- a simple toy key generation
- signing a message
- checking a signature
- why ML-DSA uses lattice problems and small errors

## Files

- `dilithium_parameters.py` - small parameters used in the examples
- `polynomial_operations.py` - basic polynomial addition and multiplication
- `toy_keygen.py` - creates a small toy public/secret key pair
- `toy_sign.py` - creates a toy signature
- `toy_verify.py` - checks the toy signature

## Note

Real ML-DSA uses larger parameters, polynomial rings, matrix operations,
sampling, rejection checks and other security mechanisms. These examples are
only meant to understand the main flow of a lattice-based signature scheme.
