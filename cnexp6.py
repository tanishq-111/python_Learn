def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += char
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += char
    return result

text = input("Enter Plain Text (Capital Letters): ")
key = int(input("Enter Key: "))

encrypted = encrypt(text, key)
print("Encrypted Text:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted Text:", decrypted)

