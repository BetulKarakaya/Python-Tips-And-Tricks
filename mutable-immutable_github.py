# MUTABLE TYPES:

# Lists
# Sets
# Dictionaries

# IMMUTABLE TYPES:

# Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
# Strings
# Tuples
# Frozen Sets




letters = ['a','b','c','d'] #Mutable variable

text = '' #Immutable variable  -> if 
#when you made a change on variable, it's memory address change because python create a copy for immutable variable and make that change on it.
print("IMMUTABLE VARIABLES")

for ltr in letters:
    text = text + ltr + ";"
    print(text)
    print(hex(id(text)))  #memory address location of the object in hexadecimal format
    #print ('Address of text variable is {}'.format(id(text)),"\n")

print("\nMUTABLE VARIABLES")
for i in range(len(letters)):
    letters[i] = '1'
    print(letters)
    print(hex(id(letters))) #memory address location of the object in hexadecimal format
    #print ('Address of letters variable is {}'.format(id(letters)),"\n")

