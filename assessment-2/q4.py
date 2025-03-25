import math 
def fermat_inverse(a, n):
    if math.gcd(a, n) != 1:
        return "Not possible using Fermat’s inverse"
    return pow(a, n - 2, n)

print("Question 4: Multiplicative Inverse using Fermat's Theorem")
a = int(input("Enter number (a): "))
n = int(input("Enter prime modulo (n): "))
result = fermat_inverse(a, n)
print(f"Multiplicative inverse of {a} mod {n} = {result}")
print()