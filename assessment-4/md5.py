def F(X, Y, Z):
    return (X & Y) | (~X & Z)

def G(X, Y, Z):
    return (X & Z) | (Y & ~Z)

def H(X, Y, Z):
    return X ^ Y ^ Z

def I(X, Y, Z):
    return Y ^ (X | ~Z)

def md5_round_functions():
    A = int("01234567", 16)
    B = int("89abcdef", 16)
    C = int("fedcba98", 16)
    D = int("76543210", 16)

    F_result = F(A, B, C)
    G_result = G(A, B, C)
    H_result = H(A, B, C)
    I_result = I(A, B, C)

    print(f"F: {hex(F_result).upper()[2:].zfill(8)}")  # Expected: FEDCBA98
    print(f"G: {hex(G_result).upper()[2:].zfill(8)}")  # Expected: 88888888
    print(f"H: {hex(H_result).upper()[2:].zfill(8)}")  # Expected: 01234567
    print(f"I: {hex(I_result).upper()[2:].zfill(8)}")  # Expected: 77777777

md5_round_functions()
