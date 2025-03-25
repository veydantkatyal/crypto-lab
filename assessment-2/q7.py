import random

def miller_rabin(n, bases):
    if n < 2:
        return "No"

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def check_composite(a, d, n, r):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False  # Probably prime
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False  # Probably prime
        return True  # Definitely composite

    for base in bases:
        if check_composite(base, d, n, r):
            return "No"  # Definitely composite

    return "Yes"  # Probably prime

# Test Cases
test_cases = [
    (4033, [2]),
    (561, [2]),
    (61, [2]),
    (4033, [2, 3])
]

for n, bases in test_cases:
    result = miller_rabin(n, bases)
    print(f"Miller-Rabin Test for n = {n}, bases = {bases} -> isPrime? {result}")
