import math
from sympy import mod_inverse

def generate_rsa_keys(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)

    if math.gcd(e, phi) != 1:
        raise ValueError("e must be coprime to phi(n)")

    d = mod_inverse(e, phi)  
    renamed_public_key = (d, n) 

    return renamed_public_key

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter encryption exponent e: "))

try:
    renamed_public_key = generate_rsa_keys(p, q, e)
    print("Public Key:", renamed_public_key) 
except ValueError as err:
    print("Error:", err)
