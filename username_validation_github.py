import string

class UserNameValidation:
    def __init__(self):
        self.min_length = 5
        self.max_length = 20
        self.min_num_count = 1
        self.min_special_char_count = 1

    def validate_user_name(self, user_name):
        return all([
            user_name[0].isalpha(),
            sum(1 for char in user_name if char == " ") == 0,
            self.min_length <= len(user_name) <= self.max_length,
            sum(1 for char in user_name if char.isdigit()) >= self.min_num_count,
            sum(1 for char in user_name if char in string.punctuation) >= self.min_special_char_count
            
        ])
    
def main():
    app = UserNameValidation()
    print(f"👤 Welcome To User Name Validation App 👤 \n")
    print(f"🟪 Validation result of betul1.  --->",app.validate_user_name("betul1."))
    print(f"🟪 Validation result of betul1  --->",app.validate_user_name("betul1"))
    print(f"🟪 Validation result of betul.  --->",app.validate_user_name("betul."))
    print(f"🟪 Validation result of bl1.  --->",app.validate_user_name("bl1."))
    print(f"🟪 Validation result of beTul.123  --->",app.validate_user_name("beTul.123"))
    print(f"🟪 Validation result of .beTul123  --->",app.validate_user_name(".beTul123"))
    print(f"🟪 Validation result of beTul. 123  --->",app.validate_user_name("beTul. 123"))
    print(f"🟪 Validation result of beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeetul1.  --->",app.validate_user_name("beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeetul1."))
if __name__ == "__main__":
    main()