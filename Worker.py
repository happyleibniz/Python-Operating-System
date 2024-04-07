import pyglet
import os


class CommandLine(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = None
        self.output_label = None
        self.label = None
        self.output_text = None
        self.user = "System"
        self.current_dir = self.user + "@PythonOS:Users/System"
        self.reset()

    def on_draw(self):
        self.clear()
        self.draw_text()

    def draw_text(self):
        self.label = pyglet.text.Label(
            self.text,
            font_name='Calibri',
            font_size=12,
            x=10,
            y=self.height - 20,
            anchor_x='left',
            anchor_y='top'
        )
        self.label.draw()

        # Display output label
        if self.output_text:
            lines = self.output_text.split('\n')
            y_position = self.label.y - self.label.content_height - 10
            for line in lines:
                while len(line) > 150:
                    self.output_label = pyglet.text.Label(
                        line[:150],
                        font_name='Calibri',
                        font_size=12,
                        x=10,
                        y=y_position,
                        anchor_x='left',
                        anchor_y='top'
                    )
                    self.output_label.draw()
                    line = line[150:]
                    y_position -= 20  # Move to the next line
                self.output_label = pyglet.text.Label(
                    line,
                    font_name='Calibri',
                    font_size=12,
                    x=10,
                    y=y_position,
                    anchor_x='left',
                    anchor_y='top'
                )
                self.output_label.draw()
                y_position -= 20  # Move to the next line

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ENTER:
            self.process_command()
            self.reset()
        elif symbol == pyglet.window.key.BACKSPACE:
            if not self.text == self.current_dir + ">":
                self.text = self.text[:-1]
        else:
            try:
                self.text += chr(symbol)
            except OverflowError:
                pass

    def process_command(self):
        command = self.text.replace(self.current_dir + ">", "").strip()
        print("Command:", command)

        # Example command handling: echo
        if command.startswith("echo"):
            self.output_text = command[5:].strip()
        elif command == "ls" or command == "dir":
            self.output_text = str(os.listdir("/"))

    def reset(self):
        self.text = self.current_dir + ">"

    def on_resize(self, width, height):
        pyglet.gl.glViewport(0, 0, width, height)


if __name__ == "__main__":
    window = CommandLine(width=800, height=600, caption="Python Command Line")
    pyglet.app.run()
