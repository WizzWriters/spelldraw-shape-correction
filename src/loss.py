from .geometry import shoelace_area, sort_clockwise, convex_intersection

def shoelace_objective(polygon1, polygon2):
	return shoelace_area(sort_clockwise(convex_intersection(polygon1, polygon2)))

def iou_objective(polygon1, polygon2):
	polygon1 = sort_clockwise(polygon1)
	polygon2 = sort_clockwise(polygon2)
	intersection_area = shoelace_area(sort_clockwise(convex_intersection(polygon1, polygon2)))
	return intersection_area / (shoelace_area(polygon1) + shoelace_area(polygon2) - intersection_area)