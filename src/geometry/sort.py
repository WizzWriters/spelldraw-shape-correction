import torch
from torch import Tensor

def sort_clockwise(points: Tensor):
	center = points.mean(dim=0)
	vectors = points - center
	# cross_products = center[0] * vectors[:, 1] - center[1] * vectors[:, 0]
	cross_products = torch.diff(vectors * center).flatten()
	dot_products = torch.sum(vectors * center, dim=1)

	angles = torch.atan2(cross_products, dot_products)
	return points[torch.sort(angles).indices]