def password_checker(password):

    requirements = [
        any(char.isdigit() for char in password),  # Does the password contain numbers?
        any(char.isupper() for char in password), # Does it contain capital letters?
        any(char.islower() for char in password), # Does it contain lowercase letters?
        any(not char.isalnum() for char in password), # # Does it contain special characters?
    ]

    return all(requirements)

if __name__ == "__main__":

    numbers = [3, 7, 12, 5]

    # The 'any()' function returns True if at least one element in the iterable is True.
    # It is useful for checking if any condition is satisfied within a list, tuple, or generator.
    print(any(num % 2 == 0 for num in numbers))  # Output: True
    
    # The 'all()' function returns True if all elements in the iterable are True.
    # It is useful for verifying if every condition is met within a list, tuple, or generator.
    print(all(num > 0 for num in numbers))  # Output: True

   
    password_false = "Python123"
    password_true = "LetsLearn!123"
    
    print(password_checker(password_false)) # Output: False
    print(password_checker(password_true)) # Output: True