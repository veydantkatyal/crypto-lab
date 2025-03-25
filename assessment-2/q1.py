import math

def mod_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    steps = []
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        steps.append(f"Base: {base}, Exp: {exp}, Result: {result}")
        exp = exp // 2
        base = (base * base) % mod
    return result, steps

# Question 1: Modulo Exponentiation
print("Question 1: Modulo Exponentiation")
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
mod = int(input("Enter modulo: "))
result, steps = mod_exponentiation(base, exp, mod)
print(f"{base}^{exp} mod {mod} = {result}")
for step in steps:
    print(step)
print()