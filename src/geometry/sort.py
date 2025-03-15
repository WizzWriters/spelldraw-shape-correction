import torch
from torch import Tensor

def sort_clockwise(points: Tensor):
	centroid = points.mean(dim=0)
	vectors = points - centroid
	angles = torch.atan2(*vectors.T)
	return points[torch.argsort(angles)]