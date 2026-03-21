# Week 5: SageMath for Post-Quantum Cryptography

## Overview

This week focuses on using SageMath for mathematical computations related to post-quantum cryptography.

The main goal is to strengthen the mathematical and computational foundations required for studying lattice-based cryptography, especially Learning With Errors (LWE) and Ring-LWE.

## Learning Objectives

By the end of Week 5, I will be able to:

- Work with SageMath for mathematical computations.
- Perform modular arithmetic and matrix operations.
- Work with vectors, matrices, and polynomial rings.
- Understand finite fields and their applications.
- Explore mathematical structures used in lattice-based cryptography.
- Implement basic cryptographic mathematical operations in SageMath.
- Connect mathematical concepts with LWE and Ring-LWE.

## Topics Covered

### Day 1 — SageMath Basics

- SageMath environment
- Variables and expressions
- Basic arithmetic
- Modular arithmetic
- Functions and calculations

### Day 2 — Vectors and Matrices

- Vectors
- Matrices
- Matrix operations
- Determinants
- Inverses
- Modular matrix arithmetic

### Day 3 — Polynomial Rings

- Polynomial rings
- Polynomial arithmetic
- Modular polynomials
- Quotient rings
- Applications to cryptography

### Day 4 — Finite Fields

- Finite fields
- Field arithmetic
- GF(p)
- Polynomial-based finite fields
- Cryptographic applications

### Day 5 — Lattice Mathematics

- Lattices
- Basis vectors
- Lattice representation
- Short vectors
- Connection between lattices and LWE

### Day 6 — SageMath and LWE

- LWE mathematical structure
- Vectors and matrices in LWE
- Noise/error vectors
- Basic LWE experimentation
- SageMath implementation

### Day 7 — Review and Mini Project

- Review of Week 5 concepts
- Mathematical experiments
- SageMath implementation
- Connection between LWE and Ring-LWE
- Preparation for Week 6

## Tools

- SageMath
- Python
- GitHub
- Jupyter Notebook

## Example SageMath Code

```python
# Modular arithmetic
a = 17
b = 23
p = 7

print((a + b) % p)
print((a * b) % p)

# Vector
v = vector(ZZ, [1, 2, 3, 4])
print(v)

# Matrix
A = matrix(ZZ, [[1, 2], [3, 4]])
print(A)
print(A.det())
