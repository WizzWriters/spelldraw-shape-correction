import torch
from collections import deque
from tkcanvas.canvas import Canvas, Event
from src.convexagon import Convexagon
from src.utils import choose_evenly


def dice_objective(polygon1: Convexagon, polygon2: Convexagon):
    return 2 * (polygon1 & polygon2).area / (polygon1.area + polygon2.area)


def fit_model(target, max_iters=1000, lr=5, params=4, early_stopping_tolerance=1e-3):
	model = choose_evenly(target, params).requires_grad_(True)
	optimizer = torch.optim.Adam([model], lr=lr)
	history = deque(maxlen=200)
	history.append((prev_loss := 1.0))

	for i in range(max_iters):
		optimizer.zero_grad()
		loss = -dice_objective(target, model)
		loss.backward()
		optimizer.step()

		loss_change = sum(history) / len(history)
		loss = abs(loss.detach().item())
		history.append(abs(prev_loss - loss))
		prev_loss = loss
		print(i, loss, loss_change)
		if loss_change < early_stopping_tolerance:
			return model
	return model


class DrawingCanvas(Canvas):
    def __init__(self, width=1200, height=1200):
        super().__init__(width=width, height=height)
        self.points = []

    @Event("<B1-Motion>")
    def on_mouse_move(self, event):
        self.reset()
        self.points.append((event.x, event.y))
        hullpoints = Convexagon(self.points).numpy()

        self.stroke_width = 1
        self.stroke_color = "gray"
        for point in self.points:
            self.point(point)

        for i in range(len(hullpoints)):
            self.line(hullpoints[i - 1], hullpoints[i])

    @Event("<ButtonPress-1>")
    def on_mouse_press(self, event):
        self.points.clear()

    @Event("<ButtonRelease-1>")
    def on_mouse_release(self, event):
        target = Convexagon(self.points)
        model = fit_model(target).detach().numpy()

        self.stroke_color = "red"
        for i in range(len(model)):
            self.line(model[i - 1], model[i])


if __name__ == "__main__":
    canvas = DrawingCanvas()
    canvas.join()
