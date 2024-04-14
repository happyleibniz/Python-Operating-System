import pyglet
import time
import sys
import importlib


class Custom_Program:
    def __init__(self, name, path, icon_type, x, y):
        """
        Icon types: .png .jpg .jpeg .svg .ico
        name (for example) : kmplayer ffpyplayer a_program
        path (for example) : C:/Uses/BlaBlaBla/Documents/Python/Disk/Programs/*Program Name*
                            or:
                            ./Disk/Programs/*Program Name*
        program example:
        ├─program_icon.png
        ├─program.py (support only .py files)
        """
        self.var = None
        self.program = None
        self.icon_sprite = None
        self.name = name
        self.path = path
        self.icon = path + "/" + self.name + "." + icon_type
        self.icon = pyglet.image.load(self.icon)
        self.x = x
        self.y = y
        self.dest_file = self.path + "/" + self.name + ".py"
        self.icon_sprite = pyglet.sprite.Sprite(
            self.icon,
            x=x,
            y=y
        )

    def show(self):
        self.icon_sprite.draw()

    def icon_is_hovered(self, x, y):
        return (
                int(self.icon_sprite.x) < x < int(self.icon_sprite.x) + self.icon_sprite.width
                and self.icon_sprite.y < y < self.icon_sprite.y + self.icon_sprite.height
        )

    def double_click(self, x, y, button, last_mouse_release, the_self):
        print(self.icon_is_hovered(x, y))
        if self.icon_is_hovered(x, y) and button == pyglet.window.mouse.LEFT:
            if hasattr(the_self, 'last_mouse_release'):
                if (x, y, button) == last_mouse_release[:-1]:
                    if time.time() - last_mouse_release[-1] < 0.2:
                        print("extending python PATHS...")
                        sys.path.insert(0, self.path)  # compile to exe needs to add to path
                        self.program = importlib.__import__(self.name)
                        self.var = self.program.Program()
                        self.blit_to_screen()
                        return True

    def blit_to_screen(self):
        try:
            self.var.blit_media()
        except Exception:
            pass

    def drag(self, x, y, dx, dy):
        if self.icon_is_hovered(x, y):
            self.x += dx
            self.y += dy
            self.icon_sprite = pyglet.sprite.Sprite(
                self.icon,
                x=self.x,
                y=self.y
            )


class Internal_Downloader:
    def __init__(self):
        pass

    def download(self):
        pass


class PNG_Shower:
    def __init__(self):
        pass
