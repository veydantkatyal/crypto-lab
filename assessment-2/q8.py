def permute(bits, table):
    return [bits[i - 1] for i in table]

def substitute(bits, sbox):
    row = int(f"{bits[0]}{bits[-1]}", 2)  
    col = int("".join(map(str, bits[1:-1])), 2)  
    return list(map(int, f"{sbox[row][col]:04b}"))  

pbox_table = [2, 4, 1, 3, 5, 7, 6, 8]
bits = list(map(int, input("Enter 8-bit binary sequence (space-separated): ").split()))

sbox = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

permuted_bits = permute(bits, pbox_table)
print("P-box Output:", permuted_bits)

sbox_input = bits[:6]
sbox_output = substitute(sbox_input, sbox)
print("S-box Output:", sbox_output)
