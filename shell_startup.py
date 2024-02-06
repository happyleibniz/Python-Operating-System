from core.utils import options, freezed_variables
import time
import pyglet
import pyglet.image
import pyglet.gl as gl
from pyglet.graphics import Batch
from Button import Button
from collections import deque

pyglet.options["shadow_window"] = False
pyglet.options["debug_gl"] = False
pyglet.options["search_local_libs"] = True
pyglet.options["audio"] = ("openal", "pulse", "directsound", "xaudio2", "silent")


class Initialization(pyglet.window.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # config
        """batches"""
        self.init_batch = Batch()
        self.LoggingGUI_batch = Batch()
        self.UserGUI_batch = Batch()
        """baches end"""
        """vars"""
        self.No_Blur_LoggingGUI = False
        self.crraima = 0
        self.loop_counter = 0  # Initialize the loop counter
        self.ANIMATION_STARTUP_COMPLETED = False
        self.InUserGUI = False
        self.loop_counter = 0  # Initialize the loop counter
        self.options = options
        """vars end"""
        """images and sprites"""
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
            y=0,
        )
        self.user_image = pyglet.image.load("core/assets/PythonOS/images/account.png")
        self.user_image_sprite = pyglet.sprite.Sprite(
            self.user_image,
            x=self.width / 2 - 150,
            y=self.height / 2,
            batch=self.LoggingGUI_batch,
        )
        self.button = Button(
            self.width / 2 - 120,
            self.height / 2 - 200,
            200,
            50,
            "LOGIN",
            self.on_button_click,
        )
        self.User = pyglet.text.Label(
            str("User"),
            font_name="calibri",
            font_size=30,
            x=self.width / 2 - 50,
            y=self.height / 2 - 100,
            batch=self.LoggingGUI_batch,
            bold=True,
        )

        self.background = pyglet.image.load("core/assets/PythonOS/images/background_black.png")
        self.background_sprite = pyglet.sprite.Sprite(img=self.background, x=0, y=0, batch=self.init_batch)
        self.WindowsLogoLeftUp = pyglet.image.load("core/assets/PythonOS/images/win1.png")
        self.WindowsLogoRightUp = pyglet.image.load("core/assets/PythonOS/images/win2.png")
        self.WindowsLogoLeftDown = pyglet.image.load("Disk/images/win3.png")
        self.WindowsLogoRightDown = pyglet.image.load("Disk/images/win4.png")

        self.WindowsLogoLeftUp_sprite = pyglet.sprite.Sprite(
            self.WindowsLogoLeftUp,
            x=self.width / 2.74,
            y=self.height / 1.5,
            batch=self.init_batch,
        )
        self.WindowsLogoRightUp_sprite = pyglet.sprite.Sprite(
            self.WindowsLogoRightUp,
            x=self.width / 2.014,
            y=self.height / 1.5,
            batch=self.init_batch,
        )
        self.WindowsLogoLeftDown_sprite = pyglet.sprite.Sprite(
            self.WindowsLogoLeftDown,
            x=self.width / 2.74,
            y=self.height / 2.3,
            batch=self.init_batch,
        )
        self.WindowsLogoRightDown_sprite = pyglet.sprite.Sprite(
            self.WindowsLogoRightDown,
            x=self.width / 2.014,
            y=self.height / 2.3,
            batch=self.init_batch,
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
        self.OS_User_GUI_IMG = pyglet.image.load("./core/assets/PythonOS/images/background_pythonOS1.jpg")
        self.OS_User_GUI = pyglet.sprite.Sprite(img=self.OS_User_GUI_IMG, x=0, y=0, batch=self.UserGUI_batch)
        self.Computer_Image = pyglet.image.load("./core/assets/PythonOS/images/computer.png")
        self.Computer_Sprite = pyglet.sprite.Sprite(img=self.Computer_Image, x=5, y=505, batch=self.UserGUI_batch)
        self.Installer_Image = pyglet.image.load("./core/assets/PythonOS/images/setup-icon.png")
        self.Installer_Sprite = pyglet.sprite.Sprite(img=self.Installer_Image, x=5, y=450, batch=self.UserGUI_batch)
        """images and sprites end"""

        self.clear()

        pyglet.clock.schedule_interval(self.update, 1 / 25)

        # # GPU command syncs
        # self.fences = deque()
        # gl.glFinish()
        # self.fences.append(gl.glFenceSync(gl.GL_SYNC_GPU_COMMANDS_COMPLETE, 0)) # Broken in pyglet 2; glFenceSync is missing

    def update(self, delta_time):
        """Every time this method is called"""
        # while len(self.fences) > self.options.MAX_CPU_AHEAD_FRAMES:
        #     fence = self.fences.popleft()
        #     gl.glClientWaitSync(fence, gl.GL_SYNC_FLUSH_COMMANDS_BIT, 2147483647)
        #     gl.glDeleteSync(fence)
        # self.clear()

        if not self.ANIMATION_STARTUP_COMPLETED:
            self.init_batch.draw()
            pyglet.clock.schedule_once(self.delayfunc1, 2)

        else:
            # Remove the sprites when animation is completed
            self.clear()
            pyglet.clock.schedule_interval(self.LoggingGUI, 1 / 114514)

    def delayfunc1(self, delay_time):
        self.ANIMATION_STARTUP_COMPLETED = True

    def LoggingGUI(self, delta_time):
        try:
            if not self.No_Blur_LoggingGUI:
                self.clear()
                self.LoggingGUI_bg.draw()
                self.LoggingGUI_batch.draw()
            else:
                self.clear()
                self.LoggingGUI_bg_img_blurred_sprite.draw()
                self.LoggingGUI_batch.draw()
                self.button.draw()
        except AttributeError:
            pass
        self.fps_text = f"PythonOS Alpha v.0.3.567 pre fps:{round(1/delta_time)}"
        pyglet.text.Label(text=self.fps_text, font_name="Calibri", x=10, y=10).draw()

    def User_GUI(self, delta_time):
        global window
        self.InUserGUI = True
        self.LoggingGUI_bg = None
        self.LoggingGUI_batch = None
        self.LoggingGUI_bg_img_blurred_sprite = None
        self.LoggingGUI_batch = None
        self.button = None
        self.clear()
        self.UserGUI_batch.draw()
        # fps_display = pyglet.window.FPSDisplay(window)
        # fps_display.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        try:
            self.computer_is_hovered = (
                int(self.Computer_Sprite.x) < x < int(self.Computer_Sprite.x) + self.Computer_Sprite.width
                and self.Computer_Sprite.y < y < self.Computer_Sprite.y + self.Computer_Sprite.height
            )
        except Exception:
            pass
        try:
            self.Installer_is_hovered = (
                int(self.Installer_Sprite.x) < x < int(self.Installer_Sprite.x) + self.Installer_Sprite.width
                and self.Installer_Sprite.y < y < self.Installer_Sprite.y + self.Installer_Sprite.height
            )
        except Exception:
            pass
        # Now you have access to the mouse coordinates
        self.MOUSE_X, self.MOUSE_Y = x, y
        # print("x: {0}, y: {1}".format(MOUSE_X, MOUSE_Y))
        try:
            self.button.on_mouse_motion(x, y, dx, dy)
        except:
            pass

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.InUserGUI:
            self.button.on_mouse_press(x, y, button, modifiers)
        if self.InUserGUI:
            if self.computer_is_hovered and button == pyglet.window.mouse.LEFT:
                print("hello there")
            if self.Installer_is_hovered and button == pyglet.window.mouse.LEFT:
                print("installer clicked")

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.computer_is_hovered:
            self.Computer_Sprite.x += dx
            self.Computer_Sprite.y += dy

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            if self.ANIMATION_STARTUP_COMPLETED:
                self.No_Blur_LoggingGUI = True

    def on_button_click(self):
        pyglet.clock.schedule_interval(self.User_GUI, 1 / 11451)

    def on_resize(self, width, height):
        gl.glViewport(0, 0, width, height)  # free resize


"""
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

"""


class Computer:
    def __init__(self):
        global window
        self.config = gl.Config(
            double_buffer=options.DOUBLE_BUFFER,
            major_version=3,
            minor_version=3,
            depth_size=options.DEPTH_SIZE,
            sample_buffers=bool(options.ANTIALIASING),
        )
        window = Initialization(
            config=self.config,
            width=options.WIDTH,
            height=options.HEIGHT,
            caption=f"PythonOS Alpha v.0.3.567 pre",
            resizable=True,
            vsync=options.VSYNC,
        )

        window.set_location(50, 60)
        window.set_icon(pyglet.image.load("core/assets/PythonOS/images/logo.png"))


if __name__ == "__main__":
    computer = Computer()
    pyglet.app.run(interval=1 / 1145)
