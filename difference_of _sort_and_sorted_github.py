
# # One small difference that can be confusing, especially for beginners, is the use of the sorted and sort functions. 
# The sorted(list) function returns a newly sorted array without changing the original list. 
# The list.sort() function sorts and updates the list directly.


new_list1 = [1,2,7,11,9,8,7,3,5]

new_list2 = new_list1

return_value1 = sorted(new_list1)
print("Return value of new_list1: ",return_value1)
print("new_list1:",new_list1)

print()

return_value2 = new_list2.sort()
print("Return value of new_list2:",return_value2)
print("new_list2:",new_list2)