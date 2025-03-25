def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, n):
    g, x, y = extended_gcd(a, n)
    if g != 1:
        return "NA"
    else:
        return x % n

print("Question 3: Multiplicative Inverse using Extended Euclidean Algorithm")
a = int(input("Enter number (a): "))
n = int(input("Enter modulo (n): "))
result = mod_inverse(a, n)
print(f"Multiplicative inverse of {a} mod {n} = {result}")
print()