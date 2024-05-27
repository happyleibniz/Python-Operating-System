import math
import pyglet
from pyglet.math import Vec2
from pyglet.image import load as load_image
from pyglet.sprite import Sprite
from pyglet import app, clock
from . import SysWindow


class Button:
    def __init__(self, x, y, image_path, label, on_click_callback=None):
        self.recta = None
        self.lbl = None
        self.f = None
        self.target = None
        self.x = x
        self.y = y
        self.img = load_image(image_path)
        self.label = label
        self.on_click_callback = on_click_callback
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

        label_x = self.logo.x + self.logo.width // 2
        label_y = self.logo.y + self.logo.height // 2
        self.lbl = pyglet.text.Label(
            self.label,
            font_size=12,
            x=label_x,
            y=label_y,
            anchor_x="center",
            anchor_y="center",
        )
        self.lbl.color = (0, 0, 0, 255)
        self.lbl.draw()

    def on_mouse_motion(self, something, x, y):
        # self.is_hovered = (
        #         self.x < x < self.x + self.logo.width and self.y < y < self.y + self.logo.height
        # )
        image_width = self.logo.width
        image_height = self.logo.height
        self.is_hovered = self.logo.x + image_width > x > self.logo.x and self.logo.y + image_height > y > self.logo.y
        # print(self.is_hovered)

    def on_mouse_press(self, something, button):
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


class DesktopButton:
    def __init__(self, x, y, image_path, label, on_click_callback=None,m_arg=("unknown",SysWindow)):
        self.drawlbl = None
        self.recta = None
        self.lbl = None
        self.f = None
        self.more_args = m_arg
        self.target = None
        self.x = x
        self.y = y
        self.img = load_image(image_path)
        self.label = label
        self.on_click_callback = on_click_callback
        self.logo = Sprite(self.img, self.x, self.y)
        self.logo.width = 64
        self.logo.height = 64
        self.width = self.logo.width
        self.height = self.logo.height
        self.is_hovered = False

    def draw(self):
        self.logo.draw()
        self.draw_lbl()

    def draw_lbl(self):
        label_x = self.logo.x + self.logo.width // 2
        label_y = self.logo.y + self.logo.height - 70
        self.slbl = pyglet.text.Label(
            self.label,
            bold=True,
            font_size=12,
            x=label_x,
            y=label_y,
            anchor_x="center",
            anchor_y="center",
        )
        self.slbl.color = (0, 0, 0, 255)
        self.slbl.draw()
        self.lbl = pyglet.text.Label(
            self.label,
            font_size=12,
            bold=True,
            x=label_x - 1.4,
            y=label_y,
            anchor_x="center",
            anchor_y="center",
        )
        self.lbl.color = (255, 255, 255, 255)
        self.lbl.draw()

    def on_mouse_motion(self, something, x, y):
        image_width = self.logo.width
        image_height = self.logo.height
        self.is_hovered = self.logo.x + image_width > x > self.logo.x and self.logo.y + image_height > y > self.logo.y
        if self.is_hovered:
            self.drawlbl = True
        else:
            self.drawlbl = False

    def on_mouse_press(self, something, button):
        if (
                self.is_hovered
                and button == pyglet.window.mouse.LEFT
                and self.on_click_callback
        ):
            self.on_click_callback(self.more_args[0],self.more_args[1])


class TaskbarButton:
    def __init__(self, x, y, image_path, label, on_click_callback=None, m_arg=("unknown",SysWindow)):
        self.recta = None
        self.lbl = None
        self.f = None
        self.target = None
        self.x = x
        self.more_args = m_arg
        self.y = y
        self.img = load_image(image_path)
        self.label = label
        self.on_click_callback = on_click_callback
        self.logo = Sprite(self.img, self.x, self.y)
        self.logo.width = 32
        self.logo.height = 32
        self.width = self.logo.width
        self.height = self.logo.height
        self.is_hovered = False
        self.drawlbl = False

    def draw(self):
        self.logo.draw()
        if self.drawlbl:
            self.draw_lbl()

    def draw_lbl(self):
        label_x = self.logo.x + self.logo.width // 2
        label_y = self.logo.y + self.logo.height + 20
        self.slbl = pyglet.text.Label(
            self.label,
            bold=True,
            font_size=12,
            x=label_x,
            y=label_y,
            anchor_x="center",
            anchor_y="center",
        )
        self.slbl.color = (0, 0, 0, 255)
        self.slbl.draw()
        self.lbl = pyglet.text.Label(
            self.label,
            font_size=12,
            bold=True,
            x=label_x - 0.5,
            y=label_y,
            anchor_x="center",
            anchor_y="center",
        )
        self.lbl.color = (255, 255, 255, 255)
        self.lbl.draw()

    def on_mouse_motion(self, something, x, y):
        image_width = self.logo.width
        image_height = self.logo.height
        self.is_hovered = self.logo.x + image_width > x > self.logo.x and self.logo.y + image_height > y > self.logo.y
        if self.is_hovered:
            self.drawlbl = True
        else:
            self.drawlbl = False

    def on_mouse_press(self, something, button):
        if (
                self.is_hovered
                and button == pyglet.window.mouse.LEFT
                and self.on_click_callback
        ):
            self.on_click_callback(self.more_args[0],self.more_args[1])
