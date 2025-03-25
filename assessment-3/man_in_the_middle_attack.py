def mitm_attack(q, alpha, XA, XB, XDA, XDB):
    YA = pow(alpha, XA, q) 
    YB = pow(alpha, XB, q) 
    
    YDA = pow(alpha, XDA, q)  
    YDB = pow(alpha, XDB, q)  
    
    KDA = pow(YA, XDA, q)  
    KDB = pow(YB, XDB, q) 

    return KDA, KDB

q = int(input("Enter prime number q: "))
alpha = int(input("Enter generator α: "))
XA = int(input("Enter private key XA: "))
XB = int(input("Enter private key XB: "))
XDA = int(input("Enter attacker's key XDA: "))
XDB = int(input("Enter attacker's key XDB: "))

KDA, KDB = mitm_attack(q, alpha, XA, XB, XDA, XDB)

print("Intercepted Key KDA:", KDA)
print("Intercepted Key KDB:", KDB)
