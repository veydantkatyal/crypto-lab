import math
from sympy import mod_inverse

def generate_rsa_keys(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)

    if math.gcd(e, phi) != 1:
        raise ValueError("e must be coprime to phi(n)")

    d = mod_inverse(e, phi)  
    public_key = (e, n)  
    private_key = (d, n)  

    return public_key, private_key

def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    if isinstance(plaintext, list):  
        return [pow(pt, e, n) for pt in plaintext if pt < n] 
    return pow(plaintext, e, n) if plaintext < n else None

p = int(input("Enter prime number P: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter encryption exponent e: "))

try:
    public_key, private_key = generate_rsa_keys(p, q, e)

    plaintext_input = input("Enter plaintext (single number or comma-separated list): ")

    if "," in plaintext_input:
        plaintext = list(map(int, plaintext_input.split(",")))
    else:
        plaintext = int(plaintext_input)

    ciphertext = rsa_encrypt(plaintext, public_key)

    if ciphertext:
        print("Ciphertext (Cᵢ):", ciphertext)
    else:
        print("Error: Plaintext value should be smaller than modulus n.")

except ValueError as err:
    print("Error:", err)
