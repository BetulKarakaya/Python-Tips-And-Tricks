import string
import random

def generate_password(length):
    """
    Generates a random password with the specified length.
    The password includes uppercase letters, lowercase letters, digits, and special characters.
    """
    if length < 6:
        return "Password too short! Choose at least 6 characters for better security."
    
    # Define character pools for the password
    uppercase = string.ascii_uppercase  # 'A-Z'
    lowercase = string.ascii_lowercase  # 'a-z'
    digits = string.digits  # '0-9'
    special_chars = string.punctuation  # '!@#$%^&*()_+-=[]{}|;:,.<>?/'

    # Combine all character pools
    all_characters = uppercase + lowercase + digits + special_chars
    
    # Ensure the password has at least one character from each pool
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to make it unpredictable
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("🔒 Welcome to the Random Password Generator!")
    try:
        # Get the desired password length from the user
        length = int(input("Enter the desired password length (minimum 6): "))
        password = generate_password(length)
        print(f"🛡️  Your randomly generated password: {password}")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
