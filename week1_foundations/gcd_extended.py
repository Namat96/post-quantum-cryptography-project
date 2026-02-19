# Day 3 - GCD and Extended Euclidean Algorithm
# Author: Namat

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

a = 30
b = 12

print("GCD:", gcd(a, b))
g, x, y = extended_gcd(a, b)
print("Extended GCD:", g, x, y)
