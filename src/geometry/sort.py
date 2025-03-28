import torch
from torch import Tensor

# def sort_clockwise(points: Tensor):
# 	centroid = points.mean(dim=0)
# 	vectors = points - centroid
# 	angles = torch.atan2(*vectors.T)
# 	return points[torch.argsort(angles)]

def sort_clockwise(points: Tensor):
    lowest_point = points[torch.argmin(points[:, 1])]    
    vectors = points - lowest_point
    angles = torch.atan2(vectors[:, 1], vectors[:, 0])    
    return points[torch.argsort(angles)]