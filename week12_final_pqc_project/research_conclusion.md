# Final Research Report

## Introduction

This project was about post-quantum cryptography. I started with the basic ideas of cryptography and mathematics and then moved toward lattice-based cryptography. The main reason for studying this area is the future threat from quantum computers to some of the cryptographic systems that are used today.

I did not try to build a complete real-world cryptographic system. My main goal was to understand the mathematics and the basic working ideas through small Python and SageMath experiments.

## What I studied

At the start of the project, I studied some basic cryptography and mathematical topics. This gave me a base for understanding public key cryptography and the problems behind it.

After that, I studied LWE. LWE is one of the important ideas in lattice-based cryptography. I learned how a small error or noise can be added to a linear equation. The noise makes it difficult to recover the secret from the available information.

I then moved to lattices and lattice reduction. I worked with basis vectors, SVP, CVP, Gram-Schmidt, and simple lattice reduction examples. These experiments helped me understand why lattice problems are important in post-quantum cryptography.

Later, I studied Ring-LWE and Module-LWE. These ideas use polynomial and module structures and are related to modern lattice-based cryptographic schemes. I also made small examples to see how polynomial operations work.

## ML-KEM / Kyber

In Week 9, I studied ML-KEM, which was previously known as Kyber. I made small toy examples for parameters, polynomial operations, key generation, encapsulation, and decapsulation.

The examples were much smaller than the real standard. This was intentional because the main purpose was learning. Working with small numbers made it easier for me to follow the calculations and see how the different parts are connected.

One thing I understood from this part is that a real cryptographic implementation is much more complicated than a simple classroom example. There are many details related to parameters, noise, security, and implementation.

## ML-DSA / Dilithium

In Week 10, I studied ML-DSA, also known as Dilithium. This part focused on lattice-based digital signatures.

I worked with simple polynomial operations and toy examples for key generation, signing, and verification. These programs helped me understand the general flow of a signature scheme.

Again, the examples are not complete implementations of the standard. They were made to understand the main concepts before moving toward more advanced research.

## Performance and security

In Week 11, I looked at some basic performance and security observations. The small Python examples were generally quick because they used small values and simple calculations.

However, this does not mean that real post-quantum systems are equally simple. Real implementations use larger parameters and need efficient algorithms. They also need careful testing because a small programming mistake can affect security.

I also learned that security and performance have to be considered together. A cryptographic system needs strong security, but it also needs to be practical enough to use.

## What I learned from the project

The biggest thing I learned is that post-quantum cryptography is closely connected with mathematics. Topics such as linear algebra, number theory, polynomials, lattices, and modular arithmetic all become useful when studying these systems.

I also became more comfortable with Python during this project. I used it for small mathematical experiments and cryptographic examples. Working on the project week by week helped me understand the topics better than only reading about them.

There are still many things I need to learn. For example, I would like to study lattice problems in more depth, learn more about the security proofs, and work with standard cryptographic libraries instead of only toy examples.

## Conclusion

This project gave me a basic practical introduction to post-quantum cryptography. I started with the foundations and gradually reached modern lattice-based schemes such as ML-KEM and ML-DSA.

The experiments in this project are simple, but they helped me understand the main ideas and how the topics are connected. I now have a better foundation for continuing my studies in lattice-based cryptography and post-quantum cryptography.

My next step is to study these topics in more mathematical depth and eventually work on a more serious research problem in post-quantum cryptography.
