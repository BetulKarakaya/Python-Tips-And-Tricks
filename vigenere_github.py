def vigenere_encrypt(text, key):
    
    #Encrypts the given text using the Vigenère Cipher with the provided key.

    encrypted = []  # Store encrypted characters
    key_repeated = (key * ((len(text) // len(key)) + 1))[:len(text)]  # Repeat the key to match text length
    
    for char, k in zip(text, key_repeated):
        if char.isalpha():  # Encrypt only alphabetic characters
            shift = ord(k.upper()) - ord('A')  # Calculate shift from the key character
            if char.isupper():
                # Using ord() to get the ASCII/Unicode code of a character
                # Using chr() to get the character from an ASCII/Unicode code
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted.append(encrypted_char)
        else:
            encrypted.append(char)  # Non-alphabetic characters remain unchanged
    
    return ''.join(encrypted)

def vigenere_decrypt(ciphertext, key):
    
    #Decrypts the given ciphertext using the Vigenère Cipher with the provided key.
    
    decrypted = []  # Store decrypted characters
    key_repeated = (key * ((len(ciphertext) // len(key)) + 1))[:len(ciphertext)]  # Repeat the key to match ciphertext length
    
    for char, k in zip(ciphertext, key_repeated):
        if char.isalpha():  # Decrypt only alphabetic characters
            shift = ord(k.upper()) - ord('A')  # Calculate shift from the key character
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)  # Non-alphabetic characters remain unchanged
    
    return ''.join(decrypted)

# Example Usage
if __name__ == "__main__":
    plaintext = "Hello, This is Vigenere Cipher!"
    key = "KEYWORD"
    
    print("Original Text:", plaintext)
    
    encrypted_text = vigenere_encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)
    
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)
