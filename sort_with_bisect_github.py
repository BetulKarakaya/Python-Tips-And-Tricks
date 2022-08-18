import bisect

#You can add a new element to the array and sort the array in one line using the insort function of the bisect library.
sorted_list = [1,7,13,16,27,32,68]

new_added_value = 11
bisect.insort(sorted_list,new_added_value)

print(sorted_list)


new_added_value = 37
bisect.insort(sorted_list,new_added_value)

print(sorted_list)

new_added_value = 61
bisect.insort(sorted_list,new_added_value)

print(sorted_list)

new_added_value = 79
bisect.insort(sorted_list,new_added_value)

print(sorted_list)

