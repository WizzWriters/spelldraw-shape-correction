from torch import Tensor, tensor
# from .sort import sort_clockwise
import torch
import numpy

def cross(p1, p2, p3):
    """Calculate the cross product of vectors OA and OB.
       A positive cross product indicates p2 counter-clockwise turn, 0 indicates p2 collinear point, and negative indicates p2 clockwise turn.
    """
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex_hull(points: Tensor):
    """Computes the convex hull of p2 set of 2D points using Graham's Scan algorithm."""
    pivot = min(points, key=lambda p: (p[0], p[1]))


    def sort_clockwise(points: Tensor):
        vectors = points - pivot
        angles = torch.atan2(*vectors.T)
        return points[torch.argsort(angles)]

    sorted_points = sort_clockwise(points)

    hull = [pivot]
    for point in sorted_points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], point) >= 0:
            hull.pop()
        hull.append(point)
    
    return tensor(numpy.array(hull))


# from scipy.spatial import ConvexHull
# def convex_hull(points: Tensor):
# 	return points[ConvexHull(points).vertices]