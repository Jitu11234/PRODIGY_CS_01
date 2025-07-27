
def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'E':
        encrypted = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    elif choice == 'D':
        decrypted = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid choice. Please enter E or D.")

if __name__ == "__main__":
    main()
