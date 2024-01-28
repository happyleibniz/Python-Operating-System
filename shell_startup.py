from core.utils import options, freezed_variables
import time
import pyglet
import pyglet.image
import pyglet.gl as gl
from pyglet.graphics import Batch
from Button import Button


class Initialization(pyglet.window.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # config
        self.init_batch = Batch()
        self.LoggingGUI_batch = Batch()
        self.No_Blur_LoggingGUI = False
        self.LoggingGUI_bg_img = pyglet.image.load("core/assets/PythonOS/images/astounding_background1.jpg")
        self.LoggingGUI_bg = pyglet.sprite.Sprite(
            self.LoggingGUI_bg_img,
            x=0,
            y=0,
        )
        self.LoggingGUI_bg_img_blurred = pyglet.image.load(
            "core/assets/PythonOS/images/astounding_background1_blured.jpg"
        )
        self.LoggingGUI_bg_img_blurred_sprite = pyglet.sprite.Sprite(
            self.LoggingGUI_bg_img_blurred,
            x=0,
            y=0
        )
        self.user_image = pyglet.image.load("core/assets/PythonOS/images/account.png")
        self.user_image_sprite = pyglet.sprite.Sprite(
            self.user_image,
            x=self.width / 2 - 150,
            y=self.height / 2,
            batch=self.LoggingGUI_batch
        )
        self.button = Button(
            self.width / 2 - 120, self.height / 2 - 200, 200, 50, "LOGIN", self.on_button_click
        )
        self.User = pyglet.text.Label(
            str("User"),
            font_name="calibri",
            font_size=30,
            x=self.width / 2 - 50,
            y=self.height / 2 - 100,
            batch=self.LoggingGUI_batch,
            bold=True
        )

        self.background = pyglet.image.load("core/assets/PythonOS/images/background_black.png")
        self.background_sprite = pyglet.sprite.Sprite(
            img=self.background, x=0, y=0, batch=self.init_batch
        )
        self.WindowsLogoLeftUp = pyglet.image.load("core/assets/PythonOS/images/win1.png")
        self.WindowsLogoRightUp = pyglet.image.load("core/assets/PythonOS/images/win2.png")
        self.WindowsLogoLeftDown = pyglet.image.load("Disk/images/win3.png")
        self.WindowsLogoRightDown = pyglet.image.load("Disk/images/win4.png")

        self.WindowsLogoLeftUp_sprite = pyglet.sprite.Sprite(
            self.WindowsLogoLeftUp,
            x=self.width / 2.74,
            y=self.height / 1.5
        )
        self.WindowsLogoRightUp_sprite = pyglet.sprite.Sprite(
            self.WindowsLogoRightUp,
            x=self.width / 2.014,
            y=self.height / 1.5
        )
        self.WindowsLogoLeftDown_sprite = pyglet.sprite.Sprite(
            self.WindowsLogoLeftDown,
            x=self.width / 2.74,
            y=self.height / 2.3
        )
        self.WindowsLogoRightDown_sprite = pyglet.sprite.Sprite(
            self.WindowsLogoRightDown,
            x=self.width / 2.014,
            y=self.height / 2.3
        )
        self.animation = pyglet.image.load_animation("core/assets/PythonOS/images/startup/startup.gif")
        bin = pyglet.image.atlas.TextureBin()
        self.animation.add_to_texture_bin(bin)
        self.init_gif_sprite = pyglet.sprite.Sprite(
            img=self.animation,
            x=self.width / 2.3,
            y=self.height / 30,
            batch=self.init_batch,
        )
        self.crraima = 0
        self.loop_counter = 0  # Initialize the loop counter
        self.ANIMATION_STARTUP_COMPLETED = False
        self.InUserGUI = False
        self.clear()
        self.loop_counter = 0  # Initialize the loop counter
        pyglet.clock.schedule_interval(
            self.update, 1 / 60
        )

    def update(self, delta_time):
        """Every time this method is called"""

        self.clear()
        self.init_batch.draw()

        if not self.ANIMATION_STARTUP_COMPLETED:
            self.WindowsLogoLeftUp_sprite.draw()
            self.WindowsLogoRightUp_sprite.draw()
            self.WindowsLogoLeftDown_sprite.draw()
            self.WindowsLogoRightDown_sprite.draw()
            pyglet.clock.schedule_once(self.delayfunc1, 3.0)

        else:
            # Remove the sprites when animation is completed
            self.clear()
            pyglet.clock.schedule_interval(
                self.LoggingGUI, 1 / 60
            )

    def delayfunc1(self, delay_time):
        self.ANIMATION_STARTUP_COMPLETED = True

    def on_mouse_motion(self, x, y, dx, dy):
        # Now you have access to the mouse coordinates
        self.MOUSE_X, self.MOUSE_Y = x, y
        # print("x: {0}, y: {1}".format(MOUSE_X, MOUSE_Y))
        try:
            self.button.on_mouse_motion(
                x,
                y,
                dx,
                dy
            )
        except:
            pass

    def on_mouse_press(self, x, y, button, modifiers):
        self.button.on_mouse_press(
            x,
            y,
            button,
            modifiers
        )

    def LoggingGUI(self, delta_time):
        if not self.No_Blur_LoggingGUI:
            self.clear()
            self.LoggingGUI_bg.draw()
            self.LoggingGUI_batch.draw()
        else:
            self.clear()
            self.LoggingGUI_bg_img_blurred_sprite.draw()
            self.LoggingGUI_batch.draw()
            self.button.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            if self.ANIMATION_STARTUP_COMPLETED:
                self.No_Blur_LoggingGUI = True

    def on_button_click(self):
        pyglet.clock.schedule_interval(self.User_GUI, 1 / 60)

    def User_GUI(self, delta_time):
        self.InUserGUI = True
        self.clear()
        print("bruh")

    def on_resize(self, width, height):
        gl.glViewport(0, 0, width, height)  # free resize


'''
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

'''


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
        self.window.set_location(50, 60)
        self.window.set_vsync(True)
        self.window.set_icon(pyglet.image.load("core/assets/PythonOS/images/logo.png"))


def main():
    initialize_logger()


if __name__ == "__main__":
    computer = Computer()
    pyglet.app.run()
