import random
import sys
import gc
from System32 import *
import pyglet


class Screen(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right_click_menu = ""
        self.DONE = False
        self.WALLPAPER = None
        self.desktop_pictures = []
        self.texture = {}
        self.texture_dir = {}
        self.dict_of_windows = {}
        self.hardware_stats = None
        self.StartProgName = ['boot']
        self.StartBootName = {"boot": Power_On_Self_Tester}
        self.Return = []
        self.HIF = 0
        self._initial_w = self.width
        self._initial_h = self.height
        self.x_scale = self.width / self._initial_w
        self.y_scale = self.height / self._initial_h
        self.window_wh_original_half = (self.width / 2 + 130, self.height / 2 + 100)
        pyglet.resource.add_font("System32/Font/AppleFont-SimplifiedChinese-1.ttf")
        self.sysimg = {
            "logo": pyglet.sprite.Sprite(img=pyglet.image.load("System32/images/logo startup.png"),
                                         x=self.width // 2 - 90, y=self.height // 2),
            "taskbar": pyglet.sprite.Sprite(img=pyglet.image.load("System32/images/taskbar.png"),
                                            x=40, y=5)
        }
        self.sysimg.get("taskbar").width -= self.sysimg.get("taskbar").x * 2
        self.sys_menus = {  # system menus
            "right click(desktop)": pyglet.sprite.Sprite(
                img=pyglet.image.load("System32/images/right click desktop.png"),
                x=0, y=0),
        }
        self.sysbtns = {
            "button": Button(x=380, y=50, image_path="System32/images/button.png", label="Login",
                             on_click_callback=self.func_d),
            "this pc": DesktopButton(x=20, y=500, image_path="System32/images/computer.png", label="Computer",
                                     on_click_callback=self.func_f, m_arg=("this pc", SysWindow())),
        }
        self.taskbar_apps = {
            'this pc': TaskbarButton(x=50, y=self.sysimg.get("taskbar").y + 1,
                                     image_path="System32/images/computer.png", label="Computer",
                                     on_click_callback=self.func_f, m_arg=("this pc", SysWindow())),
        }
        self.func_c()
        self.progress_bar = ProgressBar(self.width // 2 - 130, self.height // 2 - 40, 200, 10, 100)
        self.text = pyglet.text.Label(text="OS TESTING Hardware...",
                                      font_name=".萍方-简",
                                      font_size=10,
                                      x=self.width / 2 - 200,
                                      y=self.height / 2 - 0,
                                      bold=True,
                                      )

    def on_draw(self):
        gc.collect()
        if self.HIF == 0:
            self.clear()
            self.text.draw()
            if not self.DONE:
                for i in self.StartProgName:
                    self.StartBootName.get(i)().POST()
                    self.Return += self.StartBootName.get(i)().get_var()
                    self.text.text = "OS TESTING Hardware... Finishing>" + str(i)
                self.hardware_stats = self.Return[0]
                self.DONE = True
            pyglet.clock.schedule_once(self.func_a, delay=0)

        elif self.HIF == 1:
            self.clear()
            self.sysimg.get("logo").draw()
            self.progress_bar.draw()
            pyglet.clock.schedule_interval(self.func_b, interval=0)
        elif self.HIF == 3:
            self.texture.get(self.WALLPAPER).draw()
            pyglet.sprite.Sprite(
                img=pyglet.image.load("System32/images/" + open("System32/images/account_data.ini", 'r').read()),
                x=self.window_wh_original_half[0] / 2 + 110,
                y=self.window_wh_original_half[0] / 2,
            ).draw()  # Draw wallpaper
            self.sysbtns.get("button").draw()
            self.sysbtns.get("button").return_f(
                (self.window_wh_original_half[0] / 2 + 150, self.window_wh_original_half[0] / 2 - 150)
            )  # moving the button
            pyglet.clock.schedule_once(self.sysbtns.get("button").func_a, 1 / 60)
        elif self.HIF == 4:
            self.clear()
            self.texture.get(self.WALLPAPER).draw()
            self.sysbtns.get("this pc").draw()
            for i in list(self.dict_of_windows.keys()):
                self.dict_of_windows.get(i).draw()
            if self.right_click_menu != "":  # When the User clicked on the right button
                self.sys_menus.get("right click(desktop)").width = 100
                self.sys_menus.get("right click(desktop)").height = 100
                self.sys_menus.get("right click(desktop)").x = self.right_click_menu[0]
                self.sys_menus.get("right click(desktop)").y = self.right_click_menu[1]
                self.sys_menus.get("right click(desktop)").draw()
            self.sysimg.get("taskbar").draw()
            for i in list(self.taskbar_apps.keys()):
                self.taskbar_apps.get(i).draw()

    def func_e(self):
        dirs = ['Users/Default/Desktop']
        while dirs:
            d = dirs.pop(0)
            textures = os.listdir(d)
            for file in textures:
                if os.path.isdir(d + '/' + file):
                    dirs += [d + '/' + file]
                else:
                    pass

    def func_d(self, *args):
        self.HIF = 4

    def func_b(self, *args):
        t = self.texture
        dirs = ['System/Library/Desktop Pictures']
        while dirs:
            d = dirs.pop(0)
            textures = os.listdir(d)
            for file in textures:
                if os.path.isdir(d + '/' + file):
                    dirs += [d + '/' + file]
                else:
                    if ".png" not in file:
                        continue

                    image = pyglet.image.load(d + '/' + file)
                    n = file.split('.')[0]
                    self.texture_dir[n] = d
                    self.texture[n] = pyglet.sprite.Sprite(img=image, x=0, y=0)
                    dest_w = self.width
                    dest_h = self.height
                    self.texture[n].width = dest_w
                    self.texture[n].height = dest_h

                self.progress_bar.set_progress(self.progress_bar.progress + 1 / len(textures))
        if self.progress_bar.progress >= 1:
            for dp in self.texture.keys():
                self.desktop_pictures.append(dp)
            self.HIF = 3
            self.WALLPAPER = open("System/Library/Desktop Pictures/data.ini", "r").read()
            pyglet.clock.unschedule(self.func_b)

    def func_a(self, *args):
        self.HIF = 1

    def func_f(self, what_thing: str, window=SysWindow(), *args):
        """what_thing for example:
        -this pc
        -apple           etc."""
        if self.dict_of_windows != {}:
            if self.dict_of_windows.get(what_thing).get_draw_now():
                self.dict_of_windows.get(what_thing).now_do_not_draw()
            else:
                self.dict_of_windows.get(what_thing).now_draw()
                print(self.dict_of_windows)
        else:
            self.dict_of_windows.update({what_thing: window})
            self.dict_of_windows.get(what_thing).now_draw()
            print(self.dict_of_windows)

    def func_c(self):
        self.batch1 = pyglet.graphics.Batch()
        self.batch2 = pyglet.graphics.Batch()
        self.batch3 = pyglet.graphics.Batch()
        self.batch4 = pyglet.graphics.Batch()
        self.batch5 = pyglet.graphics.Batch()
        self.batch6 = pyglet.graphics.Batch()

    def on_resize(self, width, height):
        pyglet.gl.glViewport(0, 0, width, height)
        self.x_scale = self.width / self._initial_w
        self.y_scale = self.height / self._initial_h

    def on_mouse_release(self, x, y, button, modifiers):
        x /= self.x_scale
        y /= self.y_scale

    def on_mouse_motion(self, x, y, dx, dy):
        x /= self.x_scale
        y /= self.y_scale
        dx /= self.x_scale
        dy /= self.y_scale
        if self.HIF == 3:
            self.sysbtns.get("button").on_mouse_motion(self, x=x, y=y)
        elif self.HIF == 4:
            self.sysbtns.get("this pc").on_mouse_motion(self, x=x, y=y)
            for i in list(self.dict_of_windows.keys()):
                self.dict_of_windows.get(i).on_mouse_motion(self, x=x, y=y, dx=dx, dy=dy)
            for i in list(self.taskbar_apps.keys()):
                self.taskbar_apps.get(i).on_mouse_motion(self, x=x, y=y)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.HIF == 3:
            self.sysbtns.get("button").on_mouse_press(self, button=button)
        elif self.HIF == 4:
            self.sysbtns.get("this pc").on_mouse_press(self, button=button)
            for i in list(self.taskbar_apps.keys()):
                self.taskbar_apps.get(i).on_mouse_press(self, button=button)
            if button == pyglet.window.mouse.LEFT:
                pass
            if button == pyglet.window.mouse.RIGHT:
                self.right_click_menu = (x, y)
            else:
                self.right_click_menu = ""

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.HIF == 4:
            for i in list(self.dict_of_windows.keys()):
                self.dict_of_windows.get(i).on_mouse_drag(self, x, y, dx, dy, buttons, modifiers)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ENTER:
            pass


scr = Screen(width=data.WIDTH,
             height=data.HEIGHT,
             caption="PythonOS Alpha v.0.3.8 pre | Development code - Forest",
             resizable=data.RESIZABLE,
             vsync=data.VSYNC,
             )
pyglet.app.run(interval=0)
