import math
import pyglet
from pyglet.math import Vec2
from pyglet.image import load as load_image
from pyglet.sprite import Sprite
from pyglet import app, clock


class Button:
    def __init__(self, x, y, image_path, label, on_click_callback=None):
        self.lbl = None
        self.f = None
        self.target = None
        self.x = x
        self.y = y
        self.img = load_image(image_path)
        self.label = label
        self.on_click_callback = on_click_callback
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.width // 2
        self.logo = Sprite(self.img, self.x, self.y)
        self.width = self.logo.width
        self.height = self.logo.height
        self.is_hovered = False

    def return_f(self, target: set):
        self.target = target
        self.f = self.velocity(self.logo.position[:2], target, 150, 0.1)
        return self.f

    def velocity(self, start, end, L, k):
        d = math.dist(start, end)

        def f(x):
            return 2 * L * (1 / (1 + math.exp(-k * (x / d) * 100)) - 1 / 2)

        return f

    def draw(self):
        self.logo.draw()
        self.draw_lbl()

    def draw_lbl(self):
        self.x = self.logo.x
        self.y = self.logo.y
        self.width = self.logo.width
        self.height = self.logo.height
        label_x = self.x + self.width // 2
        label_y = self.y + self.height // 2
        self.lbl = pyglet.text.Label(
            self.label,
            font_size=12,
            x=label_x,
            y=label_y,
            anchor_x="center",
            anchor_y="center",
        )
        self.lbl.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.is_hovered = (
            self.x < x < self.x + self.width and self.y < y < self.y + self.height
        )

    def on_mouse_press(self, x, y, button, modifiers):
        if (
            self.is_hovered
            and button == pyglet.window.mouse.LEFT
            and self.on_click_callback
        ):
            self.on_click_callback()

    def func_a(self, dt):
        d = math.dist((self.logo.x, self.logo.y), self.target)
        if d != 0:
            now = Vec2(self.logo.x, self.logo.y)
            x = Vec2(*self.target) - now
            x = x.normalize() * self.f(d) * dt
            now += x
            self.logo.position = *now, 0
            self.draw_lbl()
        else:
            pass
        if d > 4:
            clock.schedule_once(self.func_a, 1 / 60)
        else:
            self.logo.position = *self.target, 0
            self.lbl.position = *self.target, 0

