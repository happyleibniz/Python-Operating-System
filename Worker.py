import pyglet
import os
import subprocess
import signal
import tarfile


class CommandLine(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password_label = None
        self.pswd_text = f"Enter password: "
        self.password = ""
        self.text = None
        self.output_label = None
        self.label = None
        self.output_text = None
        self.current_working_dir = os.getcwd()
        self.user = "System"
        self.current_dir = self.user + "@PythonOS:" + self.current_working_dir
        self.admin_mode = False  # Flag to indicate admin mode
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
        if self.admin_mode:
            self.password_label = pyglet.text.Label(
                text=self.pswd_text,
                font_name='Calibri',
                font_size=12,
                x=10,
                y=self.label.y - self.label.content_height - 20,
                anchor_x='left',
                anchor_y='top'
            )
            self.password_label.draw()

    def on_key_press(self, symbol, modifiers):
        if self.admin_mode:
            if symbol == pyglet.window.key.ENTER:
                pswd = self.pswd_text.replace("Enter password: ", "")
                print(self.pswd_text.replace("Enter password: ", ""))
                if pswd != "":
                    self.output_text = "Sorry, try again."
                else:
                    self.output_text = "processing sudo commands..."
                    self.pswd_text = ""
            elif symbol == pyglet.window.key.BACKSPACE:
                if not self.pswd_text == "Enter password: ":
                    self.pswd_text = self.pswd_text[:-1]
            else:
                try:
                    self.pswd_text += chr(symbol)
                except OverflowError:
                    pass
        else:
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
            self.output_text = "    ".join(os.listdir(self.current_working_dir))
        elif command == "pwd":
            self.output_text = self.current_working_dir
        elif command == "df":
            try:
                if os.name == 'nt':  # Check if the system is Windows
                    output = subprocess.check_output(['wmic', 'logicaldisk', 'get', 'DeviceID,FreeSpace,Size'])
                    self.output_text = self.parse_wmic_output(output)
                else:
                    output = subprocess.check_output(['df', '-h'], universal_newlines=True)
                    self.output_text = output
            except subprocess.CalledProcessError:
                self.output_text = "Failed to get disk space information."
        elif command.startswith("cd"):
            directory = command[3:].strip()
            if directory == "..":
                self.current_working_dir = os.path.dirname(self.current_working_dir)
            else:
                new_dir = os.path.join(self.current_working_dir, directory)
                if os.path.exists(new_dir) and os.path.isdir(new_dir):
                    self.current_working_dir = new_dir
                else:
                    self.output_text = "Directory not found: " + new_dir
        elif command.startswith("mkdir"):
            new_dir = command[6:].strip()
            if new_dir:
                try:
                    os.mkdir(os.path.join(self.current_working_dir, new_dir))
                except OSError as e:
                    self.output_text = f"Failed to create directory: {e}"
            else:
                self.output_text = "Usage: mkdir <directory_name>"
        elif command.startswith("sudo"):
            if not self.admin_mode:
                self.admin_mode = True
        elif command.startswith("ping"):
            host = command[5:].strip()
            if host:
                try:
                    output = subprocess.check_output(['ping', host], universal_newlines=True)
                    self.output_text = output
                except subprocess.CalledProcessError:
                    self.output_text = "Ping request failed."
            else:
                self.output_text = "Usage: ping <host>"
        elif command.startswith("kill"):
            process_id = command[5:].strip()
            if process_id:
                try:
                    pid = int(process_id)
                    os.kill(pid, signal.SIGTERM)  # Send SIGTERM signal to terminate the process
                    self.output_text = f"Process {pid} terminated successfully."
                except ValueError:
                    self.output_text = "Invalid process ID."
                except OSError as e:
                    self.output_text = f"Failed to terminate process {pid}: {e}"
            else:
                self.output_text = "Usage: kill <process_id>"
        elif command.startswith("tar"):
            args = command[4:].strip().split()
            if len(args) >= 2:
                action = args[0]
                filename = args[1]
                files = args[2:] if len(args) > 2 else []
                if action == "create":
                    self.tar_create(filename, files)
                elif action == "extract":
                    self.tar_extract(filename)
                else:
                    self.output_text = "Usage: tar <create|extract> <archive_name> [files...]"
            else:
                self.output_text = "Usage: tar <create|extract> <archive_name> [files...]"
        elif command.startswith("tree"):
            self.tree(self.current_working_dir)
        else:
            self.output_text = f"Command '{command}' not found."

        self.current_dir = self.user + "@PythonOS:" + self.current_working_dir

    def reset(self):
        self.text = self.current_dir + ">"

    def tar_create(self, filename, files):
        try:
            with tarfile.open(filename, "w") as tar:
                for file in files:
                    if os.path.isfile(file):
                        tar.add(file)
                    else:
                        self.output_text = f"File '{file}' not found or not a regular file."
        except tarfile.TarError as e:
            self.output_text = f"Failed to create tar archive: {e}"

    def tar_extract(self, filename):
        try:
            with tarfile.open(filename, "r") as tar:
                tar.extractall()
                self.output_text = f"Archive '{filename}' extracted successfully."
        except tarfile.TarError as e:
            self.output_text = f"Failed to extract tar archive: {e}"

    def tree(self, directory, level=0):
        if not os.path.isdir(directory):
            self.output_text = f"Directory '{directory}' not found or not a directory."
            return

        tree_structure = ""
        for item in sorted(os.listdir(directory)):
            path = os.path.join(directory, item)
            tree_structure += "|   " * level + "|-- " + item + "\n"
            if os.path.isdir(path):
                tree_structure += self.tree(path, level + 1)
        self.output_text = tree_structure

    def parse_wmic_output(self, output):
        lines = output.decode('utf-8').split('\n')
        result = []
        for line in lines:
            if line.strip() and "DeviceID" not in line:
                items = line.split()
                drive = items[0]
                total_space = int(items[2]) // (1024 * 1024)  # Convert to MB
                free_space = int(items[1]) // (1024 * 1024)  # Convert to MB
                result.append(f"Drive: {drive}, Total space: {total_space} MB, Free space: {free_space} MB")
        return '\n'.join(result)


if __name__ == "__main__":
    window = CommandLine(width=800, height=600, caption="Python Command Line", resizable=True)
    pyglet.app.run()
