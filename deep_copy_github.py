import copy

numbers = [1, 2, [10, 20]]

print("- Original:", numbers)

deep_copy = copy.deepcopy(numbers)
deep_copy[2].append(30)

print("- After deep copy change:")
print("  * Original:", numbers)
print("  * Deepcopy:", deep_copy)
