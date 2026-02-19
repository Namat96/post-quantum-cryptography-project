# Day 3 - Prime Checking
# Author: Nemat

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("7 is prime:", is_prime(7))
print("15 is prime:", is_prime(15))
