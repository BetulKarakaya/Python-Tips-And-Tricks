# Example showing the behavior of Python's round() function
# including the "round half to even" rule

numbers = [1.4, 1.5, 1.6, 2.5, 2.3, 2.7, 3.5, 4.5, 5.5, 6.1, 6.5, 7.5, 8.2, 8.5, 9.5]

print("Number -> round() result")
print("------------------------")

for num in numbers:
    rounded = round(num)
    print(f"{num} -> {rounded}")

# Explanation:
# 1. Normal numbers (not ending in .5) are rounded to the nearest integer
#    Example: 1.4 -> 1, 1.6 -> 2
# 2. Numbers exactly at the halfway point (ending in .5) are rounded to the nearest even number
#    Example: 1.5 -> 2, 2.5 -> 2, 3.5 -> 4
# 3. This helps balance rounding errors over large datasets
