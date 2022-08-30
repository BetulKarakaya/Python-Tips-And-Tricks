# The "is" statement controls the memory location of two variables. 
#If they represent the same area in memory, "is" returns true as the value. 
#But if our goal is to check the value of two variables, we use the "==" statement. 

# However, at this point, you should check that the variable is mutable or immutable.
# Because in immutable variables, the value of the variable points to an address. 
# This means that if we change the value of the variable, the address of the variable changes, 
# or if different variables have the same value, it points to the same address. 
# In mutable variables, if we change the value of the variable, its address will not change. In python
# -Numbers (int, float, bool,…)
# -Strings
# -Tuples
# -Frozen sets
# types are immutable variables. If mutable variables are:
# -List
# -Sets
# -Dictionaries.


# https://www.pythontutorial.net/advanced-python/python-mutable-and-immutable/

# For a better and more detailed explanation, you can check the link above.


variable1 = 15
variable2 = 15
variable3 = variable1
variable4 = 15.1

print("VAR 1", hex(id(variable1)))
print("VAR 2", hex(id(variable2)))
print("VAR 3", hex(id(variable3)))
print("VAR 4", hex(id(variable4)))

print("{v1:s} AND {v2:s} 'IS COMPORASION':".format(v1="variable1",v2="variable2") , variable1 is variable2)
print("{v1:s} AND {v2:s} '== COMPORASION':".format(v1="variable1",v2="variable2") , variable1 == variable2)

print("{v1:s} AND {v2:s} 'IS COMPORASION':".format(v1="variable1",v2="variable3") , variable1 is variable3)
print("{v1:s} AND {v2:s} '== COMPORASION':".format(v1="variable1",v2="variable3") , variable1 == variable3)

print("{v1:s} AND {v2:s} 'IS COMPORASION':".format(v1="variable1",v2="variable4") , variable1 is variable4)
print("{v1:s} AND {v2:s} '== COMPORASION':".format(v1="variable1",v2="variable4") , variable1 == variable4)

print("{v1:s} AND {v2:s} 'IS COMPORASION':".format(v1="variable2",v2="variable3") , variable2 is variable3)
print("{v1:s} AND {v2:s} '== COMPORASION':".format(v1="variable2",v2="variable3") , variable2 == variable3)

print("{v1:s} AND {v2:s} 'IS COMPORASION':".format(v1="variable2",v2="variable4") , variable2 is variable4)
print("{v1:s} AND {v2:s} '== COMPORASION':".format(v1="variable2",v2="variable4") , variable2 == variable4)



list1 = {1,2,3}
list2 = {1,2,3}
list3 = list1
list4 = {1,2,3,4}

print("LIST 1", hex(id(list1)))
print("LIST 2", hex(id(list2)))
print("LIST 3", hex(id(list3)))
print("LIST 4", hex(id(list4)))

print("{v1:s} AND {v2:s} 'IS COMPORASION':".format(v1="list1",v2="list2") , list1 is list2)
print("{v1:s} AND {v2:s} '== COMPORASION':".format(v1="list1",v2="list2") , list1 == list2)

print("{v1:s} AND {v2:s} 'IS COMPORASION':".format(v1="list1",v2="list3") , list1 is list3)
print("{v1:s} AND {v2:s} '== COMPORASION':".format(v1="list1",v2="list3") , list1 == list3)

print("{v1:s} AND {v2:s} 'IS COMPORASION':".format(v1="list1",v2="list4") , list1 is list4)
print("{v1:s} AND {v2:s} '== COMPORASION':".format(v1="list1",v2="list4") , list1 == list4)

print("{v1:s} AND {v2:s} 'IS COMPORASION':".format(v1="list2",v2="list3") , list2 is list3)
print("{v1:s} AND {v2:s} '== COMPORASION':".format(v1="list2",v2="list3") , list2 == list3)

print("{v1:s} AND {v2:s} 'IS COMPORASION':".format(v1="list2",v2="list4") , list2 is list4)
print("{v1:s} AND {v2:s} '== COMPORASION':".format(v1="list2",v2="list4") , list2 == list4)