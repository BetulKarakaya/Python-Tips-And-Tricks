#This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
#Heaps are binary trees for which every parent node has a value less than or equal to any of its children. 
#Python Documantation ,"Python heapq",https://docs.python.org/3/library/heapq.html

#If you need more explanation, you can find all the necessary information about the heap structure from the link above.

import heapq

random_numbers = [1,78,92,66,79,1,-5,17,-99]
print("SORTING NUMERIC LIST")
print(heapq.nlargest(len(random_numbers), random_numbers))  #sorting from largest to smallest
print(heapq.nsmallest(len(random_numbers), random_numbers))  #sorting from smallest to largest

# First argument is the count of how many item will output have. We can define it as size of list or smaller

print(heapq.nlargest(5, random_numbers))#
print(heapq.nsmallest(5, random_numbers))

random_letters = ["a","b","c","dddd","d", "Pyton","Awesome", "Test","a"]

print("SORTING STRING LIST")
print("WARNING NOT SORTED")
print(heapq.nlargest(len(random_letters), random_letters)) 

print("WARNING NOT SORTED")
heapq.heapify(random_letters) # Convert list to a heap
result = []
for i in range(len(random_letters)):
	result.append(heapq.heappop(random_letters))
print(result)

#It seem like heapq can not sort string value but Python use lexicographical sorting for string value. 
# (Lexicographical -> https://en.wikipedia.org/wiki/Lexicographic_order)


#The heap structure is effective in finding the smallest and largest numbers due to its tree shape.