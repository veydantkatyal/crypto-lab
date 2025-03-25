def miller_rabin(n, bases):
    if n < 2:
        return False
    for base in bases:
        if pow(base, n-1, n) != 1:
            return False
    return True

print("Question 7: Miller Rabin Primality Test")
n = int(input("Enter number to test for primality: "))
bases = list(map(int, input("Enter bases separated by space: ").split()))
result = miller_rabin(n, bases)
print(f"Is {n} prime? {result}")
print()