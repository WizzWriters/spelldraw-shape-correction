import torch
import numpy


from torch import Tensor
from src.geometry.hull import convex_hull
from src.geometry import convex_intersection
from src.geometry import sort_clockwise


class Convexagon(Tensor):
	def __new__(cls, *points):
		if len(points) == 1:
			points = points[0]
		if isinstance(points, (Tensor, Convexagon)):
			return super().__new__(cls, sort_clockwise(points))
		points = torch.tensor(
			numpy.array(points), dtype=torch.float32, requires_grad=False
		)
		return super().__new__(cls, convex_hull(points))

	def __and__(self, other: "Convexagon") -> "Convexagon":
		return Convexagon(convex_intersection(self, other))

	@property
	def area(self):
		x, y = self.T
		return 0.5 * torch.abs(torch.sum((y + y.roll(1)) * (x - x.roll(1))))

	# @classmethod
	# def __torch_function__(cls, func, types, args=(), kwargs=None):
	# 	# Check if the function is one that creates a view, like slicing or transposing
	# 	result = super(Convexagon, cls).__torch_function__(func, types, args, kwargs)

	# 	# If it's a view, ensure readjustment
	# 	if isinstance(result, Convexagon):
	# 		return Convexagon(result)

	# 	return result

	def _repr_png_(self):
		import io
		import matplotlib.pyplot as plt

		fig, ax = plt.subplots(figsize=(3, 3))
		closed_polygon = torch.cat((self, self[:1])).detach()
		ax.plot(*closed_polygon.T, linestyle="-", color="black")

		for x, y in self.detach():
			ax.scatter(x, y, color="#960000", s=16, zorder=2)
			ax.text(
				x + 0.05,
				y + 0.05,
				f"({float(x):.1f}, {float(y):.1f})",
				fontsize=10,
				color="#960000",
				zorder=3,
			)
		ax.set_xticks([])
		ax.set_yticks([])
		ax.set_frame_on(False)
		buf = io.BytesIO()
		fig.savefig(buf, format="png", bbox_inches="tight", pad_inches=0.1)
		plt.close(fig)

		return buf.getvalue()
