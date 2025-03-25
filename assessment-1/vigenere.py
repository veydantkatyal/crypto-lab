def vigenere_cipher(text, key):
    text = text.upper()
    key = key.upper()
    key = (key * (len(text) // len(key) + 1))[:len(text)]

    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i]) - ord('A')
            result += chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += text[i]
    return result

# Sample Input
plaintext = input("Enter the plaintext: ")  # Example: ATTACKATDAWN
key = input("Enter the key: ")  # Example: LEMON
ciphertext = vigenere_cipher(plaintext, key)
print("Ciphertext:", ciphertext)
