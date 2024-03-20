import os
import random
import time
import pyglet.image
from pyglet import gl
from pyglet.graphics import Batch
from pyglet.gui import ToggleButton
from core.utils import options
import win32api
import gc
import extend_modules
from collections import deque

device = win32api.EnumDisplayDevices()
settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
if options.DEBUG:
    print((device.DeviceName, device.DeviceString))
    for varname in ['Color', 'BitsPerPel', 'DisplayFrequency']:
        print(varname, ":", getattr(settings, varname))

if not options.SHADOW_WINDOW:
    pyglet.options["shadow_window"] = False
else:
    pyglet.options["shadow_window"] = True

if not options.DEBUG_GL:
    pyglet.options["debug_gl"] = False
else:
    pyglet.options["debug_gl"] = True


class Initialization(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # config
        # self.gui = pyglet.gui.GUI()
        self.asine = None
        self.button = None
        self.mc_icon_is_hovered = None
        self.installer_pg1_is_hovered = None
        self.MOUSE_Y = None
        self.MOUSE_X = None
        self.installer_is_hovered = None
        self.computer_is_hovered = None
        self.last_mouse_release = None
        self.start_up_sounds_list = []
        self.startupsound_var = 0
        self.fences = deque()
        """batches"""
        self.init_batch = Batch()
        self.logging_gui_batch = Batch()
        self.user_gui_batch = Batch()
        """batches end"""
        """vars"""
        self.installer_pg = False
        self.no_blur_logging_gui = False
        self.animation_startup_completed = False
        self.in_user_gui = False
        self.installer_pg_1_re_mc_ = False
        """vars end"""
        """images and sprites"""
        self.logging_gui_bg = pyglet.sprite.Sprite(
            pyglet.image.load("core/assets/PythonOS/images/astounding_background1.jpg"),
            x=0,
            y=0,
        )
        self.logging_gui_bg_img_blurred_sprite = pyglet.sprite.Sprite(
            pyglet.image.load("core/assets/PythonOS/images/astounding_background1_blured.jpg"),
            x=0, y=0)
        self.user_image_sprite = pyglet.sprite.Sprite(
            pyglet.image.load("core/assets/PythonOS/images/account.png"),
            x=self.width / 2 - 150,
            y=self.height / 2,
            batch=self.logging_gui_batch,
        )
        self.login_button_list = [
            pyglet.image.load("core/assets/PythonOS/images/oreui/mc_play_button.png"),
            pyglet.image.load("core/assets/PythonOS/images/oreui/mc_play_button_not_pressed.png")
        ]
        self.login_button = ToggleButton(
            x=self.width / 2 - 170,
            y=self.height / 2 - 200,
            pressed=self.login_button_list[0],
            depressed=self.login_button_list[1],
            hover=self.login_button_list[0],
            batch=self.logging_gui_batch,
        )
        self.login_button.push_handlers(on_toggle=self.login)

        self.user = pyglet.text.Label(
            "User",
            font_name="calibri",
            font_size=30,
            x=self.width / 2 - 50,
            y=self.height / 2 - 100,
            batch=self.logging_gui_batch,
            bold=True,
        )

        self.background_sprite = pyglet.sprite.Sprite(
            img=pyglet.image.load("core/assets/PythonOS/images/background_black.png"), x=0, y=0, batch=self.init_batch)
        self.WindowsLogoLeftUp = pyglet.image.load("core/assets/PythonOS/images/win1.png")
        self.WindowsLogoRightUp = pyglet.image.load("core/assets/PythonOS/images/win2.png")
        self.WindowsLogoLeftDown = pyglet.image.load("core/assets/PythonOS/images/win3.png")
        self.WindowsLogoRightDown = pyglet.image.load("core/assets/PythonOS/images/win4.png")

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
        texture_bin = pyglet.image.atlas.TextureBin()
        self.animation.add_to_texture_bin(texture_bin)
        self.init_gif_sprite = pyglet.sprite.Sprite(
            img=self.animation,
            x=self.width / 2.3,
            y=self.height / 30,
            batch=self.init_batch,
        )
        self.os_user_gui_img = pyglet.image.load("./core/assets/PythonOS/images/background_pythonOS1.jpg")
        self.os_user_gui = pyglet.sprite.Sprite(img=self.os_user_gui_img, x=0, y=0, batch=self.user_gui_batch)
        self.computer_image = pyglet.image.load("./core/assets/PythonOS/images/computer.png")
        self.computer_sprite = pyglet.sprite.Sprite(img=self.computer_image, x=5, y=505, batch=self.user_gui_batch)
        self.installer_image = pyglet.image.load("./core/assets/PythonOS/images/setup-icon.png")
        self.installer_sprite = pyglet.sprite.Sprite(img=self.installer_image, x=5, y=450, batch=self.user_gui_batch)
        self.taskbar_image = pyglet.image.load("./core/assets/PythonOS/images/taskbar.png")
        self.taskbar = pyglet.sprite.Sprite(
            img=self.taskbar_image,
            x=0,
            y=0,
            batch=self.user_gui_batch
        )
        self.installer_pg1 = pyglet.sprite.Sprite(img=pyglet.image.load("./core/assets/PythonOS/images"
                                                                        "/Installer_page1.png"), x=self.width / 5,
                                                  y=self.width / 6.5)
        self.installer_pg_1_re_mc = pyglet.sprite.Sprite(img=pyglet.image.load("./core/assets/PythonOS/images"
                                                                               "/Installer_page2.png"),
                                                         x=self.width / 5,
                                                         y=self.width / 6.5)
        self.minecraft_logo_installer = pyglet.sprite.Sprite(
            img=pyglet.image.load("./core/assets/PythonOS/images/minecraft-logo-icon.png"),
            x=self.installer_pg1.x / 0.35,
            y=self.installer_pg1.y / 0.4)
        self.minecraft_logo_installer.height = 95
        self.minecraft_logo_installer.width = 128
        self.load_sounds()
        """ ####################"""

        # Determine the size of the green rectangle based on some condition
        self.green_rectangle_width = int(self.installer_pg_1_re_mc.width / 4)  # which is 607
        self.green_rectangle_height = int(self.installer_pg_1_re_mc.height / 4)  # which is 370
        self.green_rectangle = pyglet.image.SolidColorImagePattern((50, 205, 50, 100))
        self.green_rectangle_sprite = pyglet.sprite.Sprite(pyglet.image.create(self.green_rectangle_width,
                                                                               self.green_rectangle_height,
                                                                               self.green_rectangle),
                                                           x=self.installer_pg_1_re_mc.x / 2 / 2,
                                                           y=self.installer_pg_1_re_mc.y / 2 / 2 / 2,
                                                           batch=self.user_gui_batch)
        """images and sprites end"""

        # GPU command syncs

        if not options.SMOOTH_FPS:
            self.fences.append(gl.glFenceSync(gl.GL_SYNC_GPU_COMMANDS_COMPLETE, 0))
        else:
            gl.glFinish()
        if options.ANTIALIASING:
            gl.glEnable(gl.GL_MULTISAMPLE)
            gl.glEnable(gl.GL_SAMPLE_ALPHA_TO_COVERAGE)
            gl.glSampleCoverage(0.5, gl.GL_TRUE)

    def load_sounds(self):
        print("Loading sounds")
        print("loading StartUp sounds")
        print("./core/assets/PythonOS/Media/ file names:",
              str([f for f in os.listdir("./core/assets/PythonOS/Media/") if
                   os.path.isfile(os.path.join("./core/assets/PythonOS/Media/", f))]))
        for f in os.listdir("./core/assets/PythonOS/Media/"):
            if os.path.isfile(os.path.join("./core/assets/PythonOS/Media/", f)):
                self.start_up_sounds_list.append(pyglet.media.load("./core/assets/PythonOS/Media/" + str(f)))
        print(self.start_up_sounds_list)
        self.asine = pyglet.media.load("./core/assets/PythonOS/Media/asine_shortend.wav", streaming=True)
        print("Sound load complete")

    def on_draw(self):
        while len(self.fences) > options.MAX_CPU_AHEAD_FRAMES:
            fence = self.fences.popleft()
            gl.glClientWaitSync(fence, gl.GL_SYNC_FLUSH_COMMANDS_BIT, 2147483647)
            gl.glDeleteSync(fence)
        if options.DEBUG:
            pyglet.clock.schedule_interval(self.print_fps, 1 / 480)
        if not self.animation_startup_completed:
            self.init_batch.draw()
            pyglet.clock.schedule_once(self.delayfunction1, 2)
        else:
            if not self.in_user_gui:
                try:
                    if not self.no_blur_logging_gui:
                        try:
                            if self.startupsound_var >= 0:
                                self.start_up_sounds_list[random.randint(1, len(self.start_up_sounds_list) - 1)].play()
                                gc.collect()
                                self.startupsound_var += -1
                        except pyglet.media.exceptions.MediaException:
                            pass
                        self.clear()
                        self.logging_gui_bg.draw()
                        self.logging_gui_batch.draw()
                    else:
                        self.clear()
                        self.logging_gui_bg_img_blurred_sprite.draw()
                        self.logging_gui_batch.draw()

                except AttributeError:
                    pass
            else:
                self.logging_gui_bg = None
                self.logging_gui_batch = None
                self.logging_gui_bg_img_blurred_sprite = None
                self.logging_gui_batch = None
                self.clear()
                self.user_gui_batch.draw()
                try:

                    self.minecraft_logo_installer.height = 95
                    self.minecraft_logo_installer.width = 128
                except AttributeError:
                    pass
                if self.installer_pg:
                    try:
                        for i in range(51000):
                            self.installer_pg1.opacity += 234
                        if self.installer_pg1.opacity >= 255:
                            self.installer_pg1.opacity = 255
                        self.installer_pg1.draw()
                        self.minecraft_logo_installer.draw()
                    except AttributeError:
                        pass

                else:
                    try:
                        self.installer_pg1.opacity -= 5
                        if self.installer_pg1.opacity == 5:
                            self.installer_pg1.opacity = 0
                    except AttributeError:
                        pass
                if self.installer_pg_1_re_mc_:
                    self.green_rectangle_sprite.opacity = 255
                    self.installer_pg_1_re_mc.draw()
                    if self.green_rectangle_width >= 500:
                        self.green_rectangle_sprite.opacity = 0
                        extend_modules.download_install_mc()
                    else:
                        self.green_rectangle_width = int(self.green_rectangle_width + 1)
                        self.green_rectangle = pyglet.image.SolidColorImagePattern((50, 205, 50, 100))
                        self.green_rectangle_image = pyglet.image.create(self.green_rectangle_width,
                                                                         self.green_rectangle_height,
                                                                         self.green_rectangle)
                        self.green_rectangle_sprite = pyglet.sprite.Sprite(self.green_rectangle_image,
                                                                           x=self.installer_pg_1_re_mc.x / 2 / 2,
                                                                           y=self.installer_pg_1_re_mc.y / 2 / 2 / 2,
                                                                           batch=self.user_gui_batch)
                        self.green_rectangle_sprite.draw()
                else:
                    self.green_rectangle_sprite.opacity = 0

    def delayfunction1(self, delay_time):
        self.animation_startup_completed = True

    @staticmethod
    def print_fps(delta_time):
        print(f"fps:{round(1 / delta_time)}")

    def on_mouse_motion(self, x, y, dx, dy):
        self.computer_is_hovered = (
                int(self.computer_sprite.x) < x < int(self.computer_sprite.x) + self.computer_sprite.width
                and self.computer_sprite.y < y < self.computer_sprite.y + self.computer_sprite.height
        )
        self.installer_is_hovered = (
                int(self.installer_sprite.x) < x < int(self.installer_sprite.x) + self.installer_sprite.width
                and self.installer_sprite.y < y < self.installer_sprite.y + self.installer_sprite.height
        )
        try:
            self.installer_pg1_is_hovered = (
                    int(self.installer_pg1.x) < x < int(self.installer_pg1.x) + self.installer_pg1.width
                    and self.installer_pg1.y < y < int(self.installer_pg1.y) + self.installer_pg1.height
            )
        except AttributeError:
            pass
        try:
            self.mc_icon_is_hovered = (
                    int(self.minecraft_logo_installer.x) < x < int(self.minecraft_logo_installer.x) +
                    self.minecraft_logo_installer.width and self.minecraft_logo_installer.y < y <
                    int(self.minecraft_logo_installer.y) + self.minecraft_logo_installer.height
            )
        except AttributeError:
            pass
        # Now you have access to the mouse coordinates
        self.MOUSE_X, self.MOUSE_Y = x, y
        # print("x: {0}, y: {1}".format(MOUSE_X, MOUSE_Y))
        try:
            self.button.on_mouse_motion(x, y, dx, dy)
        except AttributeError:
            pass

    def on_mouse_release(self, x, y, button, modifiers):
        self.last_mouse_release = (x, y, button, time.time())

    def login(self, toggled):
        pyglet.clock.schedule_once(self.login_mf, 2)

    def login_mf(self, delay):
        self.in_user_gui = not self.in_user_gui

    def on_mouse_press(self, x, y, button, modifiers):
        self.login_button.on_mouse_press(x, y, button, modifiers)
        if self.in_user_gui:
            if self.computer_is_hovered and button == pyglet.window.mouse.LEFT:
                if hasattr(self, 'last_mouse_release'):
                    if (x, y, button) == self.last_mouse_release[:-1]:
                        if time.time() - self.last_mouse_release[-1] < 0.2:
                            print("computer.double_click_sound")
            if self.installer_is_hovered and button == pyglet.window.mouse.LEFT:
                if hasattr(self, 'last_mouse_release'):
                    if (x, y, button) == self.last_mouse_release[:-1]:
                        if time.time() - self.last_mouse_release[-1] < 0.2:
                            print("Installer.doubleclick.sound")
                            self.installer_pg = not self.installer_pg
            if self.mc_icon_is_hovered and button == pyglet.window.mouse.LEFT:
                if hasattr(self, 'last_mouse_release'):
                    if (x, y, button) == self.last_mouse_release[:-1]:
                        if time.time() - self.last_mouse_release[-1] < 0.2:
                            self.installer_pg1 = None
                            self.minecraft_logo_installer = None
                            self.installer_pg_1_re_mc_ = True
                            self.installer_pg_1_re_mc.draw()

        try:
            if hasattr(self, 'last_mouse_release'):
                if (x, y, button) == self.last_mouse_release[:-1]:
                    """Same place, same button"""
                    if time.time() - self.last_mouse_release[-1] < 0.2:
                        print("Double-click")
        except TypeError:
            pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.computer_is_hovered:
            self.computer_sprite.x += dx
            self.computer_sprite.y += dy
        if self.installer_is_hovered:
            self.installer_sprite.x += dx
            self.installer_sprite.y += dy
        try:
            if self.installer_pg1_is_hovered:
                self.installer_pg1.x += dx
                self.installer_pg1.y += dy
                self.minecraft_logo_installer.x += dx  # Update logo position
                self.minecraft_logo_installer.y += dy  # Update logo position
        except AttributeError:
            pass

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            if self.animation_startup_completed:
                self.no_blur_logging_gui = True

    def on_resize(self, width, height):
        gl.glViewport(0, 0, width, height)


class Computer:
    def __init__(self):
        self.config = gl.Config(
            double_buffer=options.DOUBLE_BUFFER,
            major_version=3,
            minor_version=3,
            depth_size=options.DEPTH_SIZE,
            sample_buffers=bool(options.ANTIALIASING),
        )
        self.window = Initialization(
            # config=self.config,
            width=options.WIDTH,
            height=options.HEIGHT,
            caption="PythonOS Alpha v.0.3.8 pre",
            resizable=True,
            vsync=options.VSYNC,
        )

        self.window.set_location(50, 60)
        self.window.set_icon(pyglet.image.load("core/assets/PythonOS/images/logo.png"))


if __name__ == "__main__":
    computer = Computer()
    pyglet.app.run(interval=1 / int(getattr(settings, 'DisplayFrequency')))