def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


plaintext = input("Enter the plaintext: ")  
shift = int(input("Enter the shift value: ")) 
ciphertext = caesar_cipher(plaintext, shift)
print("Ciphertext:", ciphertext)
