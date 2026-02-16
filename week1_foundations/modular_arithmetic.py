# Day 1 - Modular Arithmetic Practice
# Author: Nemat

def mod_add(a, b, q):
    return (a + b) % q

def mod_mul(a, b, q):
    return (a * b) % q

def mod_pow(a, e, q):
    return pow(a, e, q)

print("Addition:", mod_add(17, 23, 5))
print("Multiplication:", mod_mul(7, 6, 11))
print("Power:", mod_pow(3, 4, 5))
