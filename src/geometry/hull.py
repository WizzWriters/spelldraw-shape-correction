from torch import Tensor
from .sort import sort_clockwise

def convex_hull(points: Tensor):
    """Compute the convex hull of 2D points using Graham scan."""
    if len(points) <= 3:
        return points
        
    sorted_points = sort_clockwise(points)
    hull = [0, 1]
    
    for i in range(2, len(sorted_points)):
        while len(hull) > 1:
            p1, p2, p3 = sorted_points[hull[-2]], sorted_points[hull[-1]], sorted_points[i]
            # Check if turn is counter-clockwise (remove point)
            if (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0:
                hull.pop()
            else:
                break
        hull.append(i)
    
    return sorted_points[hull]