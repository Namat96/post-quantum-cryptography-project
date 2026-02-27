# Quantum Threat Model

## Assumption

Adversaries may have access to large-scale, fault-tolerant quantum computers.

## Capabilities

A quantum adversary can:

- Run Shor’s Algorithm to factor large integers.
- Solve discrete logarithm problems efficiently.
- Use Grover’s Algorithm to accelerate brute-force attacks.

## Impact on Cryptography

1. Public-key cryptography based on:
   - Integer factorization (RSA)
   - Discrete logarithms (ECC, Diffie-Hellman)
   becomes insecure.

2. Symmetric cryptography (AES, hashing) remains secure
   but requires larger key sizes.

## Long-Term Risk

Encrypted data stored today may be decrypted in the future
once quantum computers become practical.

This is known as:
"Harvest now, decrypt later" attack.

## Conclusion

A transition to post-quantum cryptographic schemes
is necessary to ensure long-term security.
