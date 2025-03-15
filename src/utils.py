from torch import Tensor
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

def plot_polygons(poly1: Tensor, poly2: Tensor, axis=None, title=""):
    polygon1 = Polygon(poly1)
    polygon2 = Polygon(poly2)
    intersection = polygon1.intersection(polygon2)

    if axis is None:
        fig, ax = plt.subplots(figsize=(8, 8))

    ax.fill(*poly1.T, alpha=0.5, label='Polygon 1')
    ax.fill(*poly2.T, alpha=0.5, label='Polygon 2')

    if not intersection.is_empty:
        x, y = intersection.exterior.xy
        ax.fill(x, y, color='green', alpha=0.7, label='Intersection')

    xs, ys = poly1.T
    xc = (max(xs) + min(xs)) / 2
    yc = (max(ys) + min(ys)) / 2
    ax.set_xlim(xc - 2*(xc - min(xs)), xc + 2*(xc - min(xs)))
    ax.set_ylim(yc - 2*(yc - min(ys)), yc + 2*(yc - min(ys)))
    ax.set_aspect('equal')
    ax.legend()
    ax.set_title(title) 
    plt.grid()
    plt.show()

def choose_evenly(tensor: Tensor, m):
    return tensor[[round(k * len(tensor) / m) for k in range(m)]]