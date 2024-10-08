
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isupper():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isupper():
            decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            decrypted += chr((ord(char) - 97 - shift) % 26 + 97)

    return decrypted

def main():
    n = int(input())
    ciphertext = input()
    ciphertext1 = ciphertext.split(";")[0]
    ciphertext2 = ciphertext.split(";")[1]
    plaintext = caesar_decrypt(ciphertext1, n)
    print(plaintext)
    plaintext = caesar_decrypt(ciphertext2, n)
    print(plaintext)

if __name__ == "__main__":
    main()