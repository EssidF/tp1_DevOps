import math

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in 2D space.

    Args:
        point1 (tuple): A tuple (x1, y1) representing the coordinates of the first point.
        point2 (tuple): A tuple (x2, y2) representing the coordinates of the second point.

    Returns:
        float: The Euclidean distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Example usage:
point1 = (0, 0)
point2 = (3, 4)
distance = euclidean_distance(point1, point2)
print("Euclidean distance:", distance)
