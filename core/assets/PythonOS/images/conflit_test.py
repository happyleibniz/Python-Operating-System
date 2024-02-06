import pyglet
import ctypes
from pyglet.gl import *

window = pyglet.window.Window()

background_image = pyglet.resource.image("bg_os.png")

vertex_shader_code = """
    attribute vec4 position;
    attribute vec2 tex_coord;
    varying vec2 v_tex_coord;
    void main() {
        gl_Position = position;
        v_tex_coord = tex_coord;
    }
"""

fragment_shader_code = """
    varying vec2 v_tex_coord;
    uniform sampler2D texture;
    void main() {
        vec4 bg_color = texture2D(texture, v_tex_coord);
        vec4 text_color = vec4(1.0, 1.0, 1.0, 1.0) - bg_color;
        gl_FragColor = text_color;
    }
"""

shader_program = glCreateProgram()
vertex_shader = glCreateShader(GL_VERTEX_SHADER)
vertex_shader_code_bytes = vertex_shader_code.encode("utf-8")
glShaderSource(vertex_shader, 1, ctypes.byref(ctypes.c_char_p(vertex_shader_code_bytes)), None)
glCompileShader(vertex_shader)
glAttachShader(shader_program, vertex_shader)

fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
fragment_shader_code_bytes = fragment_shader_code.encode("utf-8")
glShaderSource(fragment_shader, 1, ctypes.byref(ctypes.c_char_p(fragment_shader_code_bytes)), None)
glCompileShader(fragment_shader)
glAttachShader(shader_program, fragment_shader)

glLinkProgram(shader_program)
glUseProgram(shader_program)

vertices = [-1, -1, 0, 0, 1, -1, 1, 0, -1, 1, 0, 1, 1, 1, 1]
vertex_list = pyglet.graphics.vertex_list(4, ("v2f", vertices), ("t2f", (0, 0, 1, 0, 0, 1, 1, 1)))


@window.event
def on_draw():
    window.clear()
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, background_image.get_texture().id)
    vertex_list.draw(GL_TRIANGLE_STRIP)
    glDisable(GL_TEXTURE_2D)


pyglet.app.run()
