import pyglet
from .Button import MenuButton

class RCMenu:
    def __init__(self, type="Desktop"):
        """types of type:
        1.Desktop
        2.Folder
        3.File
        4.Taskbar
        5.Unknown"""
        self.type = type
        self.dict_of_components = {}
        if self.type == "Unknown":
            raise Exception("Doesn't support an unknown right click menu!")
        if self.type == "Desktop":
            bg = pyglet.sprite.Sprite(
                img=pyglet.image.load("System32/images/right click desktop.png"),
                x=0, y=0),
            self.dict_of_components = {

                "change background": MenuButton(x=, y=500, image_path="System32/images/computer.png", label="Computer")
            }
            self.dict_of_components.get("bg").width = 250
            self.dict_of_components.get("bg").height = 100
        else:
            raise NotImplementedError("Not implemented")
