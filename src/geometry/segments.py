import torch
from torch import Tensor


def intersect(segment1: Tensor, segment2: Tensor) -> Tensor:
    """
    Find the intersection point of two line segments if it exists.
    
    Args:
        segment1: A list of two points [(x1, y1), (x2, y2)] representing the first line segment
        segment2: A list of two points [(x3, y3), (x4, y4)] representing the second line segment
        
    Returns:
        None if there's no intersection
        A tuple (x, y) representing the intersection point if one exists
    """
    # Extract points
    (x1, y1), (x2, y2) = segment1
    (x3, y3), (x4, y4) = segment2
    
    # Calculate denominators
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    
    # If denominator is 0, lines are parallel or collinear
    if denom == 0:
        return None
    
    # Calculate the parameters t and u
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    
    # Check if intersection is within both segments
    if 0 <= ua <= 1 and 0 <= ub <= 1:
        # Calculate intersection point
        x = x1 + ua * (x2 - x1)
        y = y1 + ua * (y2 - y1)
        return torch.stack([x, y])
    else:
        # Intersection is outside one or both segments
        return None