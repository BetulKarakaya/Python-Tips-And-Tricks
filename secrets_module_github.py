import secrets
import string

class SecurePasswordGenerator:

    def __init__(self, length=12):
        self.length = length
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate(self):
        return ''.join(secrets.choice(self.characters) for _ in range(self.length))


def main():
    generator = SecurePasswordGenerator(length=16)
    password = generator.generate()
    print(f"Generated secure password: {password}")

if __name__ == "__main__":
    main()
