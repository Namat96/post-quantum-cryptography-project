# Week 7 - Lattice Reduction and LLL

## Objectives

By the end of Week 7, I will be able to:

1. Understand why lattice basis reduction is useful.
2. Review Gram-Schmidt orthogonalization in lattice reduction.
3. Understand the basic idea of the LLL algorithm.
4. Compare an original lattice basis with a reduced basis.
5. Search for short vectors in a small lattice.

## Topics Covered

- Lattice basis quality
- Gram-Schmidt orthogonalization
- Lattice reduction
- LLL algorithm
- Short vector search
- Importance of lattice reduction in cryptography

## Tools

- Python
- NumPy
- VS Code

## Practical Experiments

1. `gram_schmidt_reduction.py` - Calculates Gram-Schmidt vectors for a small lattice basis.
2. `lll_basics.py` - Demonstrates the main ideas used in LLL reduction.
3. `lattice_reduction.py` - Performs a simple lattice basis reduction.
4. `short_vector_search.py` - Searches for short lattice vectors using small integer coefficients.
5. `lll_vs_original.py` - Compares the lengths of an original basis and a reduced basis.

## Learning Outcome

This week focuses on lattice reduction and the LLL algorithm. The experiments show how a poorly shaped basis can be changed into a shorter and more useful basis. These ideas are important in the study of lattice-based cryptography and post-quantum cryptography.

## Conclusion

Week 7 builds on the lattice concepts studied in Week 6. The main goal is to understand the practical role of lattice reduction before moving to more advanced lattice-based cryptographic constructions.
