import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("高级图形计算器")
        self.root.geometry("420x600")
        self.root.resizable(False, False)

        self.expression = ""

        self.input_text = tk.StringVar()
        self.create_ui()

    def create_ui(self):
        input_frame = tk.Frame(self.root, height=60, bg="#1c1c1c")
        input_frame.pack(pady=10, fill="x")

        input_field = tk.Entry(
            input_frame, font=('Arial', 24), textvariable=self.input_text,
            justify='right', bg="#1c1c1c", fg="#00ff99", insertbackground='white'
        )
        input_field.pack(fill='both', ipady=20)

        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        buttons = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", ".", "=", "+", "⌫"],
            ["sin", "cos", "tan", "sqrt", "^"],
            ["π", "e", "1/x", "x²", "Exit"]
        ]

        for row in buttons:
            row_frame = tk.Frame(btns_frame)
            row_frame.pack(expand=True, fill='both')
            for btn in row:
                b = tk.Button(
                    row_frame, text=btn, font=('Arial', 18), height=2, width=5,
                    bg="#2e2e2e", fg="#ffffff", activebackground="#4e4e4e",
                    command=lambda x=btn: self.on_button_click(x)
                )
                b.pack(side='left', expand=True, fill='both')

        self.root.bind('<Key>', self.on_keypress)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            self.evaluate_expression()
            return
        elif char == "⌫":
            self.expression = self.expression[:-1]
        elif char == "π":
            self.expression += str(math.pi)
        elif char == "e":
            self.expression += str(math.e)
        elif char == "sqrt":
            self.expression += "sqrt("
        elif char == "^":
            self.expression += "**"
        elif char == "1/x":
            self.expression += "1/("
        elif char == "x²":
            self.expression += "**2"
        elif char == "sin":
            self.expression += "sin("
        elif char == "cos":
            self.expression += "cos("
        elif char == "tan":
            self.expression += "tan("
        elif char == "Exit":
            self.root.quit()
        else:
            self.expression += str(char)

        self.input_text.set(self.expression)

    def evaluate_expression(self):
        try:
            expr = self.expression.replace("sqrt", "math.sqrt")
            expr = expr.replace("sin", "math.sin(math.radians")
            expr = expr.replace("cos", "math.cos(math.radians")
            expr = expr.replace("tan", "math.tan(math.radians")

            # 补全括号（因为我们加了 math.radians(
            open_count = expr.count("math.radians(")
            close_needed = open_count
            expr += ")" * close_needed

            result = eval(expr, {"__builtins__": None, "math": math})
            result = round(result, 6)
            self.input_text.set(str(result))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("错误", "表达式无效或无法计算。")
            self.expression = ""
            self.input_text.set("")

    def on_keypress(self, event):
        key = event.char
        if key in '0123456789.+-*/()':
            self.expression += key
            self.input_text.set(self.expression)
        elif event.keysym == "Return":
            self.evaluate_expression()
        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
