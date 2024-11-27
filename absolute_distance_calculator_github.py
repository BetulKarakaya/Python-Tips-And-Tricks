def absolute_distance(point1, point2):
    """
    Calculates the absolute distance between two points in 2D space.

    Parameters:
        point1 (tuple): Coordinates of the first point as (x1, y1).
        point2 (tuple): Coordinates of the second point as (x2, y2).
    
    Returns:
        float: The absolute distance between the two points.
    """
    # Calculate the absolute differences in the x and y coordinates
    x_difference = abs(point1[0] - point2[0])  # Absolute difference in x-coordinates
    y_difference = abs(point1[1] - point2[1])  # Absolute difference in y-coordinates
    
    # Calculate the total absolute distance
    total_distance = x_difference + y_difference  # Manhattan Distance
    return total_distance


# Example Usage
if __name__ == "__main__":
    # Define two points in 2D space
    point_a = (3, 7)
    point_b = (10, 2)

    # Calculate and display the absolute distance
    print(f"The total absolute distance between {point_a} and {point_b} is: {absolute_distance(point_a, point_b)}")
