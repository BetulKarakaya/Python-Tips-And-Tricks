
# sorting with sorted function

#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
test_list = [1,8,-8,9,13,4,2,11,68,8,8,7]

print(sorted(test_list))


#https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
test_tuple = ( -99,78,11,0,-1,17,68,3,1,2,88,11,13)

print(sorted(test_tuple))


# Another useful data type built into Python is the dictionary (see Mapping Types — dict). 
# Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. 
# Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. 
# Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 
# You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().
# Quote from https://docs.python.org/3/tutorial/datastructures.html#dictionaries. For form information please visit the web site.
test_dictionary = [{"city": "Python City", "citizen": 126897},{"city": "C# City", "citizen": 98219} 
,{"city": "Flutter City", "citizen": 6995}]

print(sorted(test_dictionary , key= lambda x:x["citizen"]))


#PYTHON DATA STRUCTURES PAGE YOU CAN REACH ALL ADVANCED DATA TYPE FROM THIS LINK
#https://docs.python.org/3/tutorial/datastructures.html# 
