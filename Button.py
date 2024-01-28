from pyglet import shapes
import pyglet
from pyglet import gl


class Button:
    def __init__(self, x, y, width, height, label, on_click_callback=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.on_click_callback = on_click_callback
        self.is_hovered = False

    def draw(self):
        # Draw the button rectangle
        color = (54, 45, 42, 0) if not self.is_hovered else (200, 200, 200, 255)
        shapes.Rectangle(self.x, self.y, self.width, self.height, color=color).draw()

        label_x = self.x + self.width // 2
        label_y = self.y + self.height // 2
        pyglet.text.Label(self.label, font_size=12, x=label_x, y=label_y, anchor_x='center', anchor_y='center').draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.is_hovered = self.x < x < self.x + self.width and self.y < y < self.y + self.height

    def on_mouse_press(self, x, y, button, modifiers):
        if self.is_hovered and button == pyglet.window.mouse.LEFT and self.on_click_callback:
            self.on_click_callback()

