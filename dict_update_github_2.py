from typing import Dict, Any

def merge_dicts(base: Dict[str, Any], extra: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two dictionaries and return a new one.
    base: the original dictionary
    extra: dictionary whose keys will overwrite if duplicated
    """
    merged = base.copy() 
    merged.update(extra)
    return merged

if __name__ == "__main__":

    # Example usage
    a = {"a": 1, "b": 2}
    b = {"c": 3, "d": 4}

    result = merge_dicts(a, b)
    print(result)
