import tkinter as tk
from tkinter import ttk, messagebox
import os
import subprocess

class PythonOSInstaller:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PythonOS 安装程序")
        self.window.geometry("800x400")
        self.window.iconbitmap("images/setup-icon.png")  # Set the window icon

        self.current_step = 1
        self.setup_steps = [
            self.create_version_selection_step,
            self.create_license_key_entry_step,
            # Add more steps as needed
        ]

        self.frames = []
        self.create_setup_window()

    def create_oobe_folder(self, base_path):
        data_folder = "PythonOS-data"
        oobe_path = os.path.join(base_path, data_folder)

        if not os.path.exists(oobe_path):
            os.makedirs(oobe_path)

    def on_next_button_click(self, entry, frame_index):
        input_value = entry.get()

        if input_value:
            self.create_oobe_folder(os.path.expanduser("~"))

            # Note: You can save the input value to a file or use it as needed.
            # Perform specific actions based on the current step
            if frame_index == 1:
                self.open_setup_script("setup-license-key.py")
            elif frame_index == 2:
                self.open_setup_script("setup-use.py")
            # Add more conditions for additional steps

            # Move to the next step
            self.show_frame(frame_index + 1)
        else:
            messagebox.showwarning("警告", "请提供有效的输入。")

    def open_setup_script(self, script_name):
        try:
            subprocess.Popen(["python", script_name])
        except FileNotFoundError:
            messagebox.showerror("错误", f"找不到 '{script_name}' 文件，请确保文件存在。")

    def create_setup_window(self):
        label = tk.Label(self.window, text="PythonOS 安装程序", font=("Arial", 20))
        label.pack(pady=10)
        # Create frames for each step
        for step_function in self.setup_steps:
            frame = tk.Frame(self.window)
            self.frames.append(frame)
            step_function(frame)

        # Show the initial step
        self.show_frame(0)

        # Copyright label
        copyright_label = tk.Label(self.window, text="© Github-Huangshaoqi, happyleibniz", font=("Arial", 10))
        copyright_label.place(x=10, y=365)

        self.window.mainloop()

    def show_frame(self, frame_index):
        for frame in self.frames:
            frame.pack_forget()

        self.frames[frame_index].pack()

    def create_version_selection_step(self, frame):
        version_var = tk.StringVar()
        version_var.set("正式版")  # Default version
        version_label = tk.Label(frame, text="选择版本:", font=("Arial", 16))
        version_label.pack()

        version_combobox = ttk.Combobox(frame, textvariable=version_var,
                                        values=["正式版", "专业版", "SE版", "DEV版", "BETA版"], font=("Arial", 14))
        version_combobox.pack(pady=10)

        # Next button
        next_button = tk.Button(frame, text="下一步",
                                command=lambda: self.on_next_button_click(version_combobox, 0),
                                font=("Arial", 16))
        next_button.pack(pady=10)

    def create_license_key_entry_step(self, frame):
        license_text = "输入许可密钥:\n"
        license_label_text = (
            "如果这是您第一次在此PC上安装PythonOS(或安装其他版本),\n"
            "则需要输入有效的PythonOS产品密钥。\n"
            "您的产品密钥应该在您购买PythonOS的数字副本后收到的确认电子邮件中,\n"
            "或者在Windows寄来的盒子里。\n"
            "如果您没有有效的产品密钥，请选择”我没有产品密钥”，然后您必\n须进行30天的试用，试用结束后您必须插入有效的产品密钥。"
        )
        license_text2 = "产品密钥如下所示:(xxxxx-xxxxx-xxxxx-xxxxx-xxxxx)"
        license_label = tk.Label(frame, text=license_text + "\n" + license_label_text + "\n" + license_text2,
                                 font=("Arial", 16))
        license_label.pack()

        validate_license = frame.register(self.validate_license_key)
        license_entry = tk.Entry(frame, show="", font=("Arial", 14), validate="key",
                                 validatecommand=(validate_license, "%S", "%P"))
        license_entry.pack(pady=10)

        # Next button
        next_button = tk.Button(frame, text="下一步",
                                command=lambda: self.on_next_button_click(license_entry, 1),
                                font=("Arial", 16))
        next_button.pack(pady=10)

    def validate_license_key(self, char, entry_value):
        # Custom validation function for license key
        return char.isdigit() or (char.isalpha() and char.isupper()) or char == "-"


if __name__ == "__main__":
    installer = PythonOSInstaller()
