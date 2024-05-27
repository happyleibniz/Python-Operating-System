import pyglet


class SysWindow:
    def __init__(
            self, window_size=(500, 280), window_color=(255, 255, 255), minimizable=True, resizable=True, closable=True,
            real_window_width=1000, real_window_height=562
    ):
        self.grabbed = False
        self.is_bar_hovered = False
        self.window_color = window_color
        self.init_window_size = window_size
        self.minimizable = minimizable
        self.resizable = resizable
        self.closable = closable
        self.WIDTH = real_window_width
        self.HEIGHT = real_window_height
        self.x = self.WIDTH / 3
        self.y = self.HEIGHT / 3
        self.dict_of_components = {
            "window": pyglet.shapes.Rectangle(
                self.x, self.y, self.init_window_size[0], self.init_window_size[1], color=self.window_color
            ),
            "window line": pyglet.shapes.Rectangle(self.x, self.y + (self.init_window_size[1] - 15), 1,
                                                   self.init_window_size[0], color=(0, 0, 0))
        }
        self.dict_of_components.get("window line").rotation = 90
        self.draw_now = False

    def draw(self):
        if self.draw_now:
            for i in list(self.dict_of_components.keys()):
                self.dict_of_components.get(i).draw()

    def now_draw(self):
        self.draw_now = True

    def now_do_not_draw(self):
        self.draw_now = False

    def get_draw_now(self):
        return self.draw_now

    def on_mouse_motion(self,something, x, y, dx, dy):
        bar_top = self.y + self.init_window_size[1]
        bar_bottom = self.y + self.init_window_size[1] - 15
        self.is_bar_hovered = (
            self.x < x < self.x + self.init_window_size[0] and bar_bottom < y < bar_top
        )

    def on_mouse_drag(self,something, x, y, dx, dy, buttons, modifiers):
        if self.is_bar_hovered:
            for component in self.dict_of_components.values():
                component.x += dx
                component.y += dy
            # Update the position of the window's y coordinate
            self.x += dx
            self.y += dy

