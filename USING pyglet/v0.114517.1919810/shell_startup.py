import logging
import os
import Disk.__system.options as options

import Disk.terminal
import time
import pyglet.image

__author__: str = 'Happyleibniz'
_terminal = Disk.terminal.Terminal()

import pyglet
import pyglet.gl as gl
import Disk.__system.__internal.freezed_variables as frozen_variables
from Button import Button


class InternalConfig:
    def __init__(self, options):
        self.ADVANCED_OPENGL = options.ADVANCED_OPENGL
        self.IS_WHITE = options.is_white


class Initialization(pyglet.window.Window):
    def __init__(self, **args):
        super().__init__(**args)
        # config
        config = InternalConfig(options)

        self.background = pyglet.image.load("Disk/images/background_black.png")
        self.background_sprite = pyglet.sprite.Sprite(self.background, x=0, y=0)
        self.WindowsLogoLeftUp = pyglet.image.load("Disk/images/win1.png")
        self.WindowsLogoRightUp = pyglet.image.load("Disk/images/win2.png")
        self.WindowsLogoLeftDown = pyglet.image.load("Disk/images/win3.png")
        self.WindowsLogoRightDown = pyglet.image.load("Disk/images/win4.png")
        self.button = Button(100, 100, 200, 50, "Click me", self.on_button_click)
        self.WindowsLogoLeftUp_sprite = pyglet.sprite.Sprite(self.WindowsLogoLeftUp, x=self.width / 2.74,
                                                             y=self.height / 1.5)
        self.WindowsLogoRightUp_sprite = pyglet.sprite.Sprite(self.WindowsLogoRightUp, x=self.width / 2.014,
                                                              y=self.height / 1.5)
        self.WindowsLogoLeftDown_sprite = pyglet.sprite.Sprite(self.WindowsLogoLeftDown, x=self.width / 2.74,
                                                               y=self.height / 2.3)
        self.WindowsLogoRightDown_sprite = pyglet.sprite.Sprite(self.WindowsLogoRightDown, x=self.width / 2.014,
                                                                y=self.height / 2.3)
        self.startuplist = []
        for i in range(0, 90):
            self.startuplist.append(
                pyglet.sprite.Sprite(pyglet.image.load(f"Disk/images/startup/startup_{i}.png"), x=self.width / 2.35,
                                     y=self.height / 5.5))
        self.crraima = 0
        self.loop_counter = 0  # Initialize the loop counter
        self.ANIMATION_STARTUP_COMPLETED = False
        self.clear()
        self.loop_counter = 0  # Initialize the loop counter
        pyglet.clock.schedule_interval(self.update, 1 / 60)

    def update(self, delta_time):
        """Every time this method is called"""

        self.clear()
        logging.info(f"Clearing background")
        self.background_sprite.draw()
        logging.info(f"Creating Sprites...Drawing Background Sprites")
        logging.info(f"Creating Windows Spites...Drawing Window Sprites")
        if self.ANIMATION_STARTUP_COMPLETED == False:
            self.WindowsLogoLeftUp_sprite.draw()
            self.WindowsLogoRightUp_sprite.draw()
            self.WindowsLogoLeftDown_sprite.draw()
            self.WindowsLogoRightDown_sprite.draw()
            try:
                self.startuplist[self.crraima].draw()
                self.crraima = (self.crraima + 1) % len(self.startuplist)
                if self.crraima == 1:  # Check if one loop is completed
                    self.loop_counter += 1
                    print(self.loop_counter)
                    if self.loop_counter >= 2:  # Check if two loops are completed
                        self.ANIMATION_STARTUP_COMPLETED = True
            except:
                pass
        else:

            pyglet.clock.schedule_interval(self.LoggingGUI, 1 / 60)

    def on_mouse_motion(self, x, y, dx, dy):
        # Now you have access to the mouse coordinates
        self.MOUSE_X, self.MOUSE_Y = x, y
        # print("x: {0}, y: {1}".format(MOUSE_X, MOUSE_Y))
        try:
            self.button.on_mouse_motion(x, y, dx, dy)
        except:
            pass
    def on_mouse_press(self, x, y, button, modifiers):
        self.button.on_mouse_press(x, y, button, modifiers)

    def LoggingGUI(self, delta_time):

        self.test = pyglet.text.Label(str("（恼"), font_name="calibri", font_size=30, x=self.width / 2,
                                      y=self.height / 2)

        self.button.draw()
        self.test.draw()
    def on_button_click(self):
        print("Button clicked,hello there")

    def on_resize(self, width, height):
        gl.glViewport(0, 0, width, height)


def initialize_logger():
    log_folder = "logs/"
    log_filename = f"{time.time()}.log"
    log_path = os.path.join(log_folder, log_filename)

    if not os.path.isdir(log_folder):
        os.mkdir(log_folder)
        print(f"Created {log_folder}")
    with open(log_path, "x") as file:
        file.write("[LOGS]\n")

    logging.basicConfig(level=logging.INFO, filename=log_path,
                        format="[%(asctime)s] [%(processName)s/%(threadName)s/%(levelname)s] (%(module)s.py/%("
                               "funcName)s) %(message)s")


class Computer:
    def __init__(self):
        self.config = gl.Config(double_buffer=True,
                                major_version=3, minor_version=3,
                                depth_size=32, sample_buffers=bool(options.ANTIALIASING))
        self.window = Initialization(config=self.config, width=options.WIDTH, height=options.HEIGHT,
                                     caption="PythonOS v0.114516.1919810",
                                     resizable=True, vsync=options.VSYNC)

    @staticmethod
    def start():
        pyglet.app.run(interval=0)


def main():
    initialize_logger()
    computer = Computer()
    computer.start()


if __name__ == "__main__":
    main()#(恼
