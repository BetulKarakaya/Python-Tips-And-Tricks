import numpy as np

class SmartSorter:
    """
    A class to demonstrate the power of Binary Search 
    insertion points using NumPy.
    """
    def __init__(self, sorted_array):
        # The array MUST be sorted for this function to work
        self.reference = np.array(sorted_array)

    def get_slots(self, new_items, side='left'):
        """
        TRICK: np.searchsorted()
        Finds the indices where 'new_items' should be placed 
        to maintain the sorted order of 'self.reference'.
        """
        return np.searchsorted(self.reference, new_items, side=side)

def main():

    thresholds = [10, 20, 30, 40, 50]

    test_values = [5, 15, 20, 45, 99]

    sorter = SmartSorter(thresholds)

    # Find slots using 'left' (default) and 'right'
    # 'left': if value exists, place it BEFORE the existing value (index stays same)
    # 'right': if value exists, place it AFTER the existing value (index increases)
    slots_left = sorter.get_slots(test_values, side='left')
    slots_right = sorter.get_slots(test_values, side='right')

    print("Reference Array:", thresholds)
    print("Test Values:    ", test_values)
    print("-" * 30)

    for val, s_l, s_r in zip(test_values, slots_left, slots_right):
        print(f"Value {val:2} -> Fits in Slot (Left): {s_l} | Slot (Right): {s_r}")

if __name__ == "__main__":
    main()