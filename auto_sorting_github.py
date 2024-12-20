from collections import defaultdict

def group_names_by_initial(names):
    """
    Groups names by their first letter in alphabetical order.
    """
    grouped_names = defaultdict(list)  # Creates a dictionary with lists as default values
    for name in sorted(names):  # Sorts the names alphabetically
        grouped_names[name[0].upper()].append(name)  # Groups names by their first letter (case insensitive)

    return grouped_names

def display_groups(groups):
    """
    Displays grouped names in a user-friendly format.
    """
    print("Grouped Names by Initial:")
    print("-" * 50)
    for initial, names in sorted(groups.items()):  # Ensures the display is also alphabetically ordered
        print(f"{initial}: {', '.join(names)}")  # Joins names with a comma for clean formatting

if __name__ == "__main__":
    # Example input: A mix of names
    name_list = [
        "Maria", "Melissa","Alice", "Bob", "Charlie", "Marcus","Diana", "David", "Eve", "Elizabeth", "Frank",
        "George", "Hannah", "Jacob", "Isaac", "Blair", "Isabella", "Jack", "Karen", 
        "Liam", "Xaiver", "Abraham"
    ]
    
    # Call the grouping function
    grouped = group_names_by_initial(name_list)

    # Display the results
    display_groups(grouped)
