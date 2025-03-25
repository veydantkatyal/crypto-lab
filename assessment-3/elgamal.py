import math

def elgamal_keygen(q, alpha, XA):
    YA = pow(alpha, XA, q)  
    return YA 

def elgamal_encrypt(q, alpha, YA, k, plaintext):
    C1 = pow(alpha, k, q)  
    K = pow(YA, k, q) 
    C2 = (K * plaintext) % q  
    return (C1, C2)  

q = int(input("Enter prime number q: "))
alpha = int(input("Enter generator α: "))
XA = int(input("Enter private key XA: "))
k = int(input("Enter random integer k: "))
plaintext = int(input("Enter plaintext: "))

YA = elgamal_keygen(q, alpha, XA)

ciphertext = elgamal_encrypt(q, alpha, YA, k, plaintext)

print("Public Key (YA):", YA)
print("Ciphertext (Cᵢ):", ciphertext)
