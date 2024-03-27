#Straight from chatGPT
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift uppercase letters
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift lowercase letters
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text

# Get user input
plaintext = input("Enter text to encrypt: ")

# Encrypt the user input using Caesar cipher with a right shift of 5
encrypted_text = caesar_cipher_encrypt(plaintext, 5)

# Print the encrypted text
print("Encrypted text:", encrypted_text)
