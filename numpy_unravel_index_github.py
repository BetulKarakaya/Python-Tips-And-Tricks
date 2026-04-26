import numpy as np

class SpatialLocator:
    """
    A class to translate flattened indices back into 
    multi-dimensional coordinate systems.
    """
    def __init__(self, shape):
        self.shape = shape # e.g., (1000, 1000)

    def locate_peak(self, flat_index):
        """
        TRICK: np.unravel_index()
        It converts a flat index into a tuple of coordinate indices
        based on the original matrix dimensions.
        """
        coords = np.unravel_index(flat_index, self.shape)
        return coords

def main():
   
    grid_shape = (100, 100)
    risk_grid = np.random.rand(*grid_shape)

    
    target_row, target_col = 42, 87
    risk_grid[target_row, target_col] = 50.0  # The extreme outlier

    #Find the index of the maximum value in the FLATTENED array
    # argmax() returns a single integer, not a coordinate.
    flat_max_idx = np.argmax(risk_grid)
    print(f"Flat Index Found: {flat_max_idx}")

    #Use our Locator to find the (Row, Col)
    locator = SpatialLocator(grid_shape)
    actual_coords = locator.locate_peak(flat_max_idx)

    print(f"\n--- Coordinate Recovery ---")
    print(f"Calculated Coordinates: Row {actual_coords[0]}, Col {actual_coords[1]}")
    print(f"Original Planted Site: Row {target_row}, Col {target_col}")
    
    if actual_coords == (target_row, target_col):
        print("Success: The spatial mapping is perfect!")

if __name__ == "__main__":
    main()