# In Python, the zip() function pairs elements from two different lists or tuples.
# This example demonstrates how to use the zip() function to pair two different feature lists such as names and ages.

# Sample lists of names and ages
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]

# Pairing names and ages lists using the zip() function
for name, age in zip(names, ages):
    print(name, "is", age, "years old")
