""" Disclaimer:

The code provided here demonstrates the usage of the exec() function in Python for 
educational purposes only. By providing this code, no responsibility or liability is 
assumed for any consequences arising from its use. The user is solely responsible for 
understanding the risks associated with executing dynamic code and should exercise 
caution when running code provided by others.

 """

# This Python program allows the user to input Python code and executes it using the exec() function.
# It provides a simple interface for running arbitrary Python code snippets.

# Advantages of using exec():
# 1. Flexibility: Allows dynamic execution of Python code provided by the user.
# 2. Interactivity: Enables interactive programming, allowing users to experiment with code snippets.

# Disadvantages of using exec():
# 1. Security Risks: Running untrusted or malicious code can lead to security vulnerabilities.
# 2. Readability: Executed code may be harder to understand and debug compared to static code.
# 3. Performance: Dynamic code execution may have performance implications compared to pre-compiled code.


# Prompting the user to input Python code
code = input("Enter the Python code you want to execute: ")

# Executing the user-provided code
try:
    exec(code)
except Exception as e:
    print("An error occurred:", e)


""" Disclaimer:

The code provided here demonstrates the usage of the exec() function in Python for 
educational purposes only. By providing this code, no responsibility or liability is 
assumed for any consequences arising from its use. The user is solely responsible for 
understanding the risks associated with executing dynamic code and should exercise 
caution when running code provided by others.

 """
