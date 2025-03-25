def playfair_cipher(text, key):
    # Create key matrix
    key = ''.join(dict.fromkeys(key.replace('J', 'I').upper()))  # Remove duplicates, replace J with I, and convert to uppercase
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Playfair excludes J
    matrix = [c for c in key if c in alphabet] + [c for c in alphabet if c not in key]
    key_square = [matrix[i:i+5] for i in range(0, 25, 5)]

    # Helper functions
    def find_position(char):
        for i, row in enumerate(key_square):
            if char in row:
                return i, row.index(char)
        raise ValueError(f"Character '{char}' not found in key square!")  # Raise error if character not found

    def encode_pair(a, b):
        row1, col1 = find_position(a)
        row2, col2 = find_position(b)
        if row1 == row2:
            return key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            return key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
        else:
            return key_square[row1][col2] + key_square[row2][col1]

    # Prepare text
    text = text.upper().replace('J', 'I').replace(' ', '')
    prepared_text = ''
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            prepared_text += text[i] + 'X'
            i += 1
        else:
            prepared_text += text[i] + text[i + 1]
            i += 2
    if len(prepared_text) % 2 != 0:
        prepared_text += 'X'

    # Encode text
    result = ''
    for i in range(0, len(prepared_text), 2):
        result += encode_pair(prepared_text[i], prepared_text[i + 1])
    return result


# Sample Input
plaintext = input("Enter the plaintext: ")  # Example: HELLO
key = input("Enter the key: ")  # Example: MONARCHY
try:
    ciphertext = playfair_cipher(plaintext, key)
    print("Ciphertext:", ciphertext)
except ValueError as e:
    print("Error:", e)
