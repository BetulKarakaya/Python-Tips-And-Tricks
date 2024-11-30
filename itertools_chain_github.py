from itertools import chain

def flatten_nested_lists(nested_lists):
    """
    Flattens a list of nested lists into a single flat list using itertools.chain.
    
    Args:
        nested_lists (list of lists): A list containing multiple sub-lists.
        
    Returns:
        list: A single flat list with all elements.
    """
    # Use chain to combine all inner lists into a single iterable
    flat_list = list(chain(*nested_lists))
    return flat_list

if __name__ == "__main__":
    # Example nested lists
    nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    
    print("Nested Lists:")
    print(nested)
    
    # Flatten the nested lists
    flat = flatten_nested_lists(nested)
    
    print("\nFlattened List:")
    print(flat)
