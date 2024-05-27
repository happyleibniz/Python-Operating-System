import pyglet


class ProgressBar:
    def __init__(self, x, y, width, height, radius):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius
        self.progress = 0

        # Create batch for drawing
        self.batch = pyglet.graphics.Batch()
        # Background rectangle
        self.bg_rect = self.create_rounded_rectangle(x, y, width, height, radius, (0, 0, 0))
        # Progress rectangle
        self.progress_rect = self.create_rounded_rectangle(x, y, 0, height, radius, (255, 255, 255))

    def set_progress(self, progress):
        self.progress = max(0, min(progress, 1))
        self.progress_rect.width = self.width * self.progress

    def create_rounded_rectangle(self, x, y, width, height, radius, color):
        rectangle = pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=self.batch)
        rectangle.radius = radius
        return rectangle

    def draw(self):
        self.batch.draw()