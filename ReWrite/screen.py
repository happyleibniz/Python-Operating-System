import random
import sys
import gc
from System32 import *
import pyglet


class Screen(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DONE = False
        self.WALLPAPER = None
        self.desktop_pictures = []
        self.texture = {}
        self.texture_dir = {}
        self.hardware_stats = None
        self.StartProgName = ['boot']
        self.StartBootName = {"boot": Power_On_Self_Tester}
        self.Return = []
        self.HIF = 0
        self.window_wh_original_half = (self.width / 2 + 130, self.height / 2 + 100)
        pyglet.resource.add_font("System32/Font/AppleFont-SimplifiedChinese-1.ttf")
        self.sysimg = {
            "logo": pyglet.sprite.Sprite(img=pyglet.image.load("System32/images/logo startup.png"),
                                         x=self.width // 2 - 90, y=self.height // 2),
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
            ).draw()
            self.libt.draw()
            self.libt.return_f((self.window_wh_original_half[0] / 2 + 100, self.window_wh_original_half[0] / 2 - 100))
            pyglet.clock.schedule_once(self.libt.func_a, 1 / 60)

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
            print(sys.getsizeof(self.texture))
            self.WALLPAPER = open("System/Library/Desktop Pictures/data.ini", "r").read()
            pyglet.clock.unschedule(self.func_b)

    def func_a(self, *args):
        self.HIF = 1

    def func_c(self):
        self.batch1 = pyglet.graphics.Batch()
        self.batch2 = pyglet.graphics.Batch()
        self.batch3 = pyglet.graphics.Batch()
        self.batch4 = pyglet.graphics.Batch()
        self.batch5 = pyglet.graphics.Batch()
        self.batch6 = pyglet.graphics.Batch()
        self.libt = Button(
            x=380, y=50, image_path="System32/images/test.png", label="klasdfjlkadjflasdfl"
        )

    def on_resize(self, width, height):
        pyglet.gl.glViewport(0, 0, width, height)


scr = Screen(width=data.WIDTH,
             height=data.HEIGHT,
             caption="PythonOS Alpha v.0.3.8 pre | Development code - Forest",
             resizable=data.RESIZABLE,
             vsync=data.VSYNC,
             )
pyglet.app.run(interval=0)
