import math
def euler_inverse(a, n):
    if math.gcd(a, n) != 1:
        return "NA"
    phi_n = n - 1  # For prime n, phi(n) = n-1
    return pow(a, phi_n - 1, n)

print("Question 5: Multiplicative Inverse using Euler's Theorem")
a = int(input("Enter number (a): "))
n = int(input("Enter modulo (n): "))
result = euler_inverse(a, n)
print(f"Multiplicative inverse of {a} mod {n} = {result}")
print()