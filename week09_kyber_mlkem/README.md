# Week 9 - Kyber / ML-KEM Basics

## Introduction
This week moves from Ring-LWE and Module-LWE to the Kyber family of lattice-based key encapsulation mechanisms. The examples here are small educational experiments, not a production implementation of Kyber or ML-KEM.

## Topics
- Kyber and ML-KEM overview
- Polynomial and module arithmetic used by the scheme
- A small toy key generation experiment
- Encapsulation and decapsulation idea
- Noise and error terms
- Why the real ML-KEM algorithm uses carefully chosen parameters and security checks

## Files
- `kyber_parameters.py` - small parameter set used in the experiments
- `toy_keygen.py` - toy public/private key generation
- `toy_encapsulation.py` - toy encapsulation example
- `toy_decapsulation.py` - toy decapsulation example
- `noise_experiment.py` - simple noise experiment
- `README.md` - notes for the week

## Important note
The code is intentionally small so the main ideas can be followed. It is **not** a secure implementation of Kyber/ML-KEM and should not be used for real encryption or key exchange.

## Learning outcome
The main goal of this week is to understand how Module-LWE ideas appear inside a KEM and how public keys, secret values, noise, encapsulation and decapsulation fit together.
