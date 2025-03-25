import numpy as np

def hill_cipher(text, key_matrix):
    text = text.upper()
    n = len(key_matrix)
    while len(text) % n != 0:
        text += 'X'  # Padding with X

    text_vector = [ord(char) - ord('A') for char in text]

    result = []
    for i in range(0, len(text_vector), n):
        block = text_vector[i:i+n]
        cipher_block = np.dot(key_matrix, block) % 26
        result.extend(cipher_block)

    ciphertext = ''.join(chr(int(num) + ord('A')) for num in result)
    return ciphertext

def get_key_matrix():
    size = int(input("Enter the size of the key matrix (e.g., 2 for 2x2, 3 for 3x3): "))
    print(f"Enter the key matrix (row by row, space-separated values):")
    key_matrix = []
    for i in range(size):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != size:
            raise ValueError("Invalid key matrix. Each row must have the same number of elements as the matrix size.")
        key_matrix.append(row)
    return key_matrix

plaintext = input("Enter the plaintext: ")  # Example: HELLO
key_matrix = get_key_matrix()  # Take key matrix input from user
ciphertext = hill_cipher(plaintext, key_matrix)
print("Ciphertext:", ciphertext)
