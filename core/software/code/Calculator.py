import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("计算器")
        self.geometry("400x500")
        self.result_var = tk.StringVar()

        # Set window icon
        icon_image = tk.PhotoImage(file="images/Calculator.png")
        self.iconphoto(True, icon_image)

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=('Segoe UI', 14), padding=10)

        entry_frame = ttk.Frame(self)
        entry_frame.grid(row=0, column=0, columnspan=4)

        entry = ttk.Entry(entry_frame, textvariable=self.result_var, font=('Segoe UI', 20), justify="right")
        entry.grid(row=0, column=0, sticky="nsew")
        entry_frame.columnconfigure(0, weight=1)

        button_layout = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for text, row, col in button_layout:
            button = ttk.Button(self, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

            self.grid_rowconfigure(row, weight=1)
            self.grid_columnconfigure(col, weight=1)

    def on_button_click(self, value):
        if value == 'C':
            self.result_var.set('')
        elif value == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('错误')
        else:
            current_text = self.result_var.get()
            current_text += value
            self.result_var.set(current_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
