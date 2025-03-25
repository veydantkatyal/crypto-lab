def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1

def dss_sign():
    p, q = map(int, input("Enter (p, q): ").strip('()').split(','))
    k = int(input("Enter k: "))
    h = int(input("Enter h(M): "))
    private_key = int(input("Enter private key: "))
    h_M = int(input("Enter h(M): "))
    g = int(input("Enter g: "))
    public_key = int(input("Enter public key: "))

    # Signature generation
    r = pow(g, k, p) % q
    k_inv = mod_inverse(k, q)
    s = (k_inv * (h_M + private_key * r)) % q
    print(f"(r, s) = ({r},{s})")

    # Verification process
    w = mod_inverse(s, q)
    u1 = (h_M * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(public_key, u2, p)) % p) % q
    print(f"(u1, u2) = ({u1},{u2})")

    if v == r:
        print("Accepted")
    else:
        print("Rejected")

dss_sign()
