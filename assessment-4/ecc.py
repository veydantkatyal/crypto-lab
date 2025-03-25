def point_addition(P, Q, a, p):
    if P == Q:
        m = (3 * P[0] ** 2 + a) * pow(2 * P[1], -1, p) % p
    else:
        m = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p) % p
    x3 = (m ** 2 - P[0] - Q[0]) % p
    y3 = (m * (P[0] - x3) - P[1]) % p
    return (x3, y3)

def ecc_encrypt():
    p = int(input("Enter prime number (p): "))
    a = int(input("Enter curve parameter (a): "))
    b = int(input("Enter curve parameter (b): "))
    G_x, G_y = map(int, input("Enter generator point (Gx, Gy): ").split())
    nB = int(input("Enter private key (nB): "))
    k = int(input("Enter random integer (k): "))
    M_x, M_y = map(int, input("Enter message point (Mx, My): ").split())

    G = (G_x, G_y)
    M = (M_x, M_y)

    Pb = G
    for _ in range(nB - 1):
        Pb = point_addition(Pb, G, a, p)

    C1 = G
    for _ in range(k - 1):
        C1 = point_addition(C1, G, a, p)

    C2 = M
    for _ in range(k):
        C2 = point_addition(C2, Pb, a, p)

    print(f"Public key: PB = {Pb}")
    print(f"Ciphertext: C1 = {C1}, C2 = {C2}")

ecc_encrypt()
