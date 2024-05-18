## DEVELOPER MANUAL

### Main.py
```text
{variable}          {why do i need to call that}
inith                    : window initialize height
initw                    : window initialize width
nowh                     : (after resizing) window height
noww                     : (after resizing) window width
self.installer_pg1       : installer page 1
self.installer_pg_1_re_mc: installing mc
self.startupsound_var    : startup sound variable
self.resize_plusw        : (after resizing) if noww > initw : resize_plusw = noww - initw
```

#### GPU Sync
```python
from collections import deque
from pyglet.gl import gl as gl
fences = deque()
fence = fences.popleft()
gl.glClientWaitSync(fence, gl.GL_SYNC_FLUSH_COMMANDS_BIT, 2147483647)
gl.glDeleteSync(fence)
```

#### how to use custom program(has lots of bugs, still alpha)
```python
import Custom_Program as CPs
program = CPs.Custom_Program(
        name="kmplayer",  # for example
        path="./Disk/Programs/KMPlayer",  # for example
        icon_type="png", x=100, y=100  # for example
    )
# using Custom Program:
show_program_window = False
def on_draw(self):
    program.show()
    if show_program_window:
        program.blit_to_screen()
        
def on_mouse_press(self, x, y, button, modifiers):
    if self.program.double_click(
        x, y, button,
        self.last_mouse_release,
        the_self=self):
        show_program_window = True
        
def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
    self.program.drag(x, y, dx, dy)
```

# continued...
###### email: happyleibniz@outlook.com
###### license: MIT (Note:Some versions are in The Unlicense)
###### for more info, see https://github.com/happyleibniz/Python-Operating-System-Unlicensed