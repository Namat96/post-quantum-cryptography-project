# Motivation for Post-Quantum Cryptography

## The Quantum Threat

The development of large-scale quantum computers poses a serious threat
to modern cryptographic systems.

Shor’s Algorithm breaks:
- RSA
- ECC
- Diffie-Hellman

Grover’s Algorithm reduces the effective security
of symmetric cryptography.

## The Problem

Most internet security protocols today rely on RSA and ECC.

If quantum computers become practical,
these systems will become insecure.

Additionally, encrypted data collected today
may be decrypted in the future once quantum computers exist.
This is known as:

"Harvest Now, Decrypt Later"

## The Solution

Post-Quantum Cryptography (PQC) aims to design
cryptographic schemes secure against quantum attacks.

Lattice-based cryptography,
especially Learning With Errors (LWE),
is one of the most promising approaches.

## Research Direction

This project studies LWE and Ring-LWE
as quantum-resistant alternatives to classical cryptography.
