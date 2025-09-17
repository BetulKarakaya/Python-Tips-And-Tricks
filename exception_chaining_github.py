import re

class UserRegistration:
    def __init__(self, email: str):
        self.email = email

    def validate_email(self):
        """Check if email is in a valid format"""
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError("❌ Invalid email format")
        return True

    def save_to_db(self):
        """Simulate saving to a database (always fails for demo)"""
        raise ConnectionError("❌ Database connection failed")

    def register(self):
        try:
            self.validate_email()
            self.save_to_db()
        except ValueError as e:
            raise RuntimeError("Registration failed due to invalid input") from e
        except ConnectionError as e:
            raise RuntimeError("Registration failed due to system error") from e


def main():
    # Test 1 → invalid email
    try:
        user = UserRegistration("user_at_mail.com")
        user.register()
    except RuntimeError as e:
        print("Error:", e)

    # Test 2 → valid email but DB error
    try:
        user = UserRegistration("user@example.com")
        user.register()
    except RuntimeError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
