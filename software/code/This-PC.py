import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
import cv2

class FileManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("文件资源管理器")

        # Set the initial directory to the "system" folder
        self.current_directory = os.path.join(os.getcwd(), "disk")

        # Create a toolbar
        self.toolbar = ttk.Frame(self.master)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.refresh_button = ttk.Button(self.toolbar, text="刷新", command=self.refresh_files)
        self.refresh_button.pack(side=tk.LEFT)

        self.open_button = ttk.Button(self.toolbar, text="打开选定的文件夹", command=self.open_selected_folder)
        self.open_button.pack(side=tk.LEFT)

        self.go_back_button = ttk.Button(self.toolbar, text="返回上一级", command=self.go_back)
        self.go_back_button.pack(side=tk.LEFT)

        self.text_display = tk.Text(self.master, wrap=tk.WORD, height=10, width=40)
        self.text_display.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)

        self.save_button = ttk.Button(self.toolbar, text="保存", command=self.save_text_content)
        self.save_button.pack(side=tk.LEFT)

        # Create the file listbox below the toolbar
        self.file_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.file_listbox.pack(expand=tk.YES, fill=tk.BOTH)

        # Bind right-click event to show context menu
        self.file_listbox.bind("<Button-3>", self.show_context_menu)
        self.context_menu = tk.Menu(self.master, tearoff=0)
        self.context_menu.add_command(label="新建文本文档", command=self.create_text_document)
        self.context_menu.add_command(label="新建文件夹", command=self.create_folder)
        self.context_menu.add_command(label="复制", command=self.copy_selected)
        self.context_menu.add_command(label="打开", command=self.open_selected_folder)
        self.context_menu.add_command(label="删除", command=self.delete_selected)
        self.context_menu.add_command(label="重命名", command=self.rename_selected)

        # Bind double-click event to open folder
        self.file_listbox.bind("<Double-Button-1>", self.double_click_file)

        self.refresh_files()

    def refresh_files(self):
        files_and_folders = os.listdir(self.current_directory)

        self.file_listbox.delete(0, tk.END)
        for item in files_and_folders:
            self.file_listbox.insert(tk.END, item)

    def open_selected_folder(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_item = self.file_listbox.get(selected_index)
            selected_path = os.path.join(self.current_directory, selected_item)
            
            if os.path.isdir(selected_path):
                self.current_directory = selected_path
                self.refresh_files()
            else:
                tk.messagebox.showinfo("错误", "选定的项目不是文件夹。")

    def show_context_menu(self, event):
        selected_index = self.file_listbox.nearest(event.y)
        self.file_listbox.selection_clear(0, tk.END)
        self.file_listbox.selection_set(selected_index)
        self.context_menu.post(event.x_root, event.y_root)

    def copy_selected(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_item = self.file_listbox.get(selected_index)
            selected_path = os.path.join(self.current_directory, selected_item)

            # Store the path of the selected item in a class variable
            self.copied_path = selected_path

    def save_text_content(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_item = self.file_listbox.get(selected_index[0])
            selected_path = os.path.join(self.current_directory, selected_item)

            try:
                content = self.text_display.get("1.0", tk.END)
                with open(selected_path, "w", encoding="latin-1") as file:
                    file.write(content)
                messagebox.showinfo("保存成功", "文件保存成功。")
            except Exception as e:
                messagebox.showerror("保存失败", f"保存文件失败: {str(e)}")

    def go_back(self):
        print(f"Before - Current Directory: {self.current_directory}")
        if os.path.normpath(self.current_directory) != os.path.normpath(os.path.join(os.getcwd(), "disk")):
            parent_directory = os.path.dirname(self.current_directory)
            print(f"Going back to: {parent_directory}")

            self.current_directory = os.path.abspath(parent_directory)
            self.refresh_files()

        print(f"After - Current Directory: {self.current_directory}")

    def double_click_file(self, event):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_item = self.file_listbox.get(selected_index[0])
            selected_path = os.path.join(self.current_directory, selected_item)

            if os.path.isdir(selected_path):
                self.current_directory = selected_path
                self.refresh_files()
            elif selected_path.lower().endswith((".txt", ".py", ".html", ".bat", ".cmd")):
                self.display_text_content(selected_path)  # 对于支持的文件类型显示内容
            elif selected_path.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                self.open_image_file(selected_path)  # 对于图片文件打开图片
            else:
                self.text_display.delete(1.0, tk.END)  # 对于不支持的文件类型清除文本显示

    def open_image_file(self, image_path):
        try:
            image = Image.open(image_path)
            img_tk = ImageTk.PhotoImage(image)
            
            # 创建一个新的顶级窗口来显示图像
            img_window = tk.Toplevel(self.master)
            img_window.title("Image Viewer")

            # 将图像放在窗口上
            label = tk.Label(img_window, image=img_tk)
            label.pack()

            # 关闭图像窗口时释放图像资源
            img_window.protocol("WM_DELETE_WINDOW", lambda: img_window.destroy())
            
            img_window.mainloop()
        except Exception as e:
            messagebox.showerror("错误", f"无法打开图片文件: {str(e)}")


    def create_text_document(self):
        # Implement the creation of a new text document here
        new_text_file = os.path.join(self.current_directory, "新建文本文档.txt")
        with open(new_text_file, "w") as file:
            pass  # Just creating an empty file for demonstration
        self.refresh_files()

    def create_folder(self):
        # Implement the creation of a new folder here
        new_folder = os.path.join(self.current_directory, "新建文件夹")
        os.makedirs(new_folder)
        self.refresh_files()

    def delete_selected(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_item = self.file_listbox.get(selected_index)
            selected_path = os.path.join(self.current_directory, selected_item)

            try:
                if os.path.isdir(selected_path):
                    os.rmdir(selected_path)
                else:
                    os.remove(selected_path)
            except Exception as e:
                messagebox.showerror("错误", f"删除失败: {str(e)}")

            self.refresh_files()

    def rename_selected(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_item = self.file_listbox.get(selected_index)
            selected_path = os.path.join(self.current_directory, selected_item)

            new_name = askstring("重命名", "请输入新名称：", initialvalue=selected_item)
            if new_name:
                new_path = os.path.join(self.current_directory, new_name)

                try:
                    os.rename(selected_path, new_path)
                except Exception as e:
                    messagebox.showerror("错误", f"重命名失败: {str(e)}")

                self.refresh_files()

def main():
    root = tk.Tk()
    app = FileManagerApp(root)
    root.geometry("700x450")
    root.mainloop()

if __name__ == "__main__":
    main()
