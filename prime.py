""" A prime number is a positive integer that is divisible only by itself
    and one. If an integer can be factored into smaller numbers, we call it
    a composite numberself.
Prime num: (2, 3, 5, 7, 11, 13, 17, ...)
Composite num: (4, 6, 8, 9, ...)
"""
import time
import math # to take square root of n
def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. 'false' otherwise."""
    if n == 1:
        return False # 1 is not prime
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. 'false' otherwise."""
    if n == 1:
        return False # 1 is not prime
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. 'false' otherwise."""
    if n == 1:
        return False # 1 is not prime
    # If it's  even and not 2, then it's not prime
    if n == 2:
        return True # 2 is prime number
    if n > 2 and n % 2 == 0:
        return False
    max_divisor_2 = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor_2, 2):
        if n % d == 0:
            return False
    return True
# ==== Time Function 3 ====

t4 = time.time()
for n in range(1, 100000):
    is_prime_v3(n)
t5 = time.time()
print("time required for V3: ", t5 - t4)

# ==== Time Function 2 ====

t0 = time.time()
for n in range(1, 100000):
    is_prime_v2(n)
t1 = time.time()
print("time required for V2: ", t1 - t0)

# ==== Time Function 1 ====

t2 = time.time()
for n in range(1, 100000):
    is_prime_v1(n)
t3 = time.time()
print("time required for V1: ", t3 - t2)
