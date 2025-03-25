def sha512_pad():
    message = input("Enter message: ")
    message = ''.join(format(ord(c), '08b') for c in message)
    message += '1'

    while len(message) % 1024 != 896:
        message += '0'

    length_bits = format(len(message) - 1, '0128b')
    padded_message = message + length_bits

    print("Padded Message (Binary):", padded_message)

sha512_pad()
