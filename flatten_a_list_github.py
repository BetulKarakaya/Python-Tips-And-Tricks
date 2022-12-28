#how to flatten a list that have tuple items

list_with_tuples = [(1, 2, 3, 4), (5, 6, 7), (8, 9),("a","b","d")]

flattened_list = []

list(flattened_list.extend(item) for item in list_with_tuples)

print('Original list', list_with_tuples)
print('Transformed list', flattened_list)
