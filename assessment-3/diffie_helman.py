def diffie_hellman(q, alpha, XA, XB):
    YA = pow(alpha, XA, q)  
    YB = pow(alpha, XB, q) 
    
    keyA = pow(YB, XA, q)  
    keyB = pow(YA, XB, q)  
    
    if keyA == keyB:
        return keyA 
    else:
        raise ValueError("Key exchange failed, keys do not match!")

q = int(input("Enter prime number q: "))
alpha = int(input("Enter generator α: "))
XA = int(input("Enter private key XA: "))
XB = int(input("Enter private key XB: "))

try:
    shared_key = diffie_hellman(q, alpha, XA, XB)
    print("Shared Key:", shared_key) 
except ValueError as err:
    print("Error:", err)
