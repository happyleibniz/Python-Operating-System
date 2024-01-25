from core.utils import options, freezed_variables

import pyglet
import pyglet.image
import pyglet.gl as gl
from pyglet.graphics import Batch


class Initialization(pyglet.window.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # config
        self.main_batch = Batch()

        background = pyglet.image.load("core/images/background_black.png")
        self.background_sprite = pyglet.sprite.Sprite(
            img=background, x=0, y=0, batch=self.main_batch
        )
        WindowsLogoLeftUp = pyglet.image.load("core/images/win1.png")
        WindowsLogoRightUp = pyglet.image.load("core/images/win2.png")
        WindowsLogoLeftDown = pyglet.image.load("core/images/win3.png")
        WindowsLogoRightDown = pyglet.image.load("core/images/win4.png")
        self.WindowsLogoLeftUp_sprite = pyglet.sprite.Sprite(
            WindowsLogoLeftUp,
            x=self.width / 2.74,
            y=self.height / 1.5,
            batch=self.main_batch,
        )
        self.WindowsLogoRightUp_sprite = pyglet.sprite.Sprite(
            WindowsLogoRightUp,
            x=self.width / 2.014,
            y=self.height / 1.5,
            batch=self.main_batch,
        )
        self.WindowsLogoLeftDown_sprite = pyglet.sprite.Sprite(
            WindowsLogoLeftDown,
            x=self.width / 2.74,
            y=self.height / 2.3,
            batch=self.main_batch,
        )
        self.WindowsLogoRightDown_sprite = pyglet.sprite.Sprite(
            WindowsLogoRightDown,
            x=self.width / 2.014,
            y=self.height / 2.3,
            batch=self.main_batch,
        )
        animation = pyglet.image.load_animation("core/images/startup/startup.gif")
        bin = pyglet.image.atlas.TextureBin()
        animation.add_to_texture_bin(bin)
        self.init_gif_sprte = pyglet.sprite.Sprite(
            img=animation,
            x=self.width / 2.35,
            y=self.height / 5.5,
            batch=self.main_batch,
        )
        self.crraima = 0
        self.ANIMATION_STARTUP_COMPLETED = False
        self.clear()
        pyglet.clock.schedule_interval(self.update, 1 / 60)

    def update(self, delta_time):
        """Every time this method is called"""
        self.clear()
        self.main_batch.draw()

    def on_resize(self, width, height):
        super().on_resize(width, height)


class Computer:
    def __init__(self):
        self.config = gl.Config(
            double_buffer=True,
            major_version=3,
            minor_version=3,
            depth_size=32,
            sample_buffers=bool(options.ANTIALIASING),
        )
        self.window = Initialization(
            config=self.config,
            width=options.WIDTH,
            height=options.HEIGHT,
            caption="PythonOS v0.114515.1919810",
            resizable=True,
            vsync=options.VSYNC,
        )


if __name__ == "__main__":
    computer = Computer()
    pyglet.app.run()
