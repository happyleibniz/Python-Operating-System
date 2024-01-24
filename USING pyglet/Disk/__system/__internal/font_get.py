import pyglet


def GetFont(FontName, FontSize):
    pyglet.resource.add_font(FontName)
    font = pyglet.font.load(FontName, int(FontSize))
    return font
