import torch
from torch import Tensor

def shoelace_area(vertices: Tensor):
    x, y = vertices.T
    return 0.5 * torch.abs(torch.sum((y + y.roll(1)) * (x - x.roll(1))))
