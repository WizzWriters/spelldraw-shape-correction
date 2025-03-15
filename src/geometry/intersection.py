import torch
from torch import Tensor
from shapely.geometry import Polygon

from .segments import intersect
from itertools import product

def convex_intersection(polygon1: Tensor, polygon2: Tensor):
	poly1 = Polygon(polygon1.detach())
	poly2 = Polygon(polygon2.detach())
	intersection = poly1.intersection(poly2)
	vertices = list(intersection.exterior.coords)

	output = [
		*[v for v in polygon1 if tuple(v.detach()) in vertices],
		*[v for v in polygon2 if tuple(v.detach()) in vertices]
	]

	for segment1, segment2 in product(
		zip(polygon1, polygon1.roll(1, dims=0)),
		zip(polygon2, polygon2.roll(1, dims=0))
	):
		inter = intersect(segment1, segment2)
		if inter is not None:
			output.append(inter)

	return torch.stack(output)