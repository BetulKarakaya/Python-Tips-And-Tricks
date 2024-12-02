import string

def encrypt_message(message, shift):
    """
    Encrypts a message using Caesar Cipher with the given shift.

    Parameters:
        message (str): The message to encrypt.
        shift (int): The number of positions to shift each character.

    Returns:
        str: The encrypted message.
    """
    # The Caesar Cipher replaces each letter with a letter some fixed number of positions down the alphabet.
    # Step 1: Get all lowercase and uppercase letters (a-z, A-Z) using the 'string' module.
    alphabet = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Step 2: Create the shifted alphabet.
    # Example: If shift = 2, 'abc' becomes 'cde'.
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Step 3: Create a translation table for mapping original to shifted characters.
    # Example: {'a': 'c', 'b': 'd', ...}.
    table = str.maketrans(alphabet, shifted_alphabet)

    # Step 4: Use the 'translate' method to replace characters based on the translation table.
    return message.translate(table)

def decrypt_message(encrypted_message, shift):
    """
    Decrypts a message encrypted with Caesar Cipher.

    Parameters:
        encrypted_message (str): The encrypted message.
        shift (int): The number of positions the original message was shifted.

    Returns:
        str: The decrypted message.
    """
    # To decrypt, reverse the shift by using a negative shift value.
    return encrypt_message(encrypted_message, -shift)

if __name__ == "__main__":
    # Example Usage:
    original_message = "Hello World, It's Betül Karakaya!"  # The message to encrypt
    shift = 5  # The number of positions to shift the alphabet

    # Step 1: Encrypt the original message using Caesar Cipher
    encrypted = encrypt_message(original_message, shift)
    print(f"🔐 Encrypted Message: {encrypted}")  # Outputs the encrypted text

    # Step 2: Decrypt the encrypted message to retrieve the original
    decrypted = decrypt_message(encrypted, shift)
    print(f"🔓 Decrypted Message: {decrypted}")  # Outputs the original text
