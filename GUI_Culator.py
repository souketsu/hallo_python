import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("图形界面计算器")  # 设置窗口标题
        self.root.geometry("400x500")    # 设置窗口大小
        self.root.resizable(False, False)  # 禁止窗口缩放

        self.expression = ""  # 用于保存当前输入的表达式

        self.input_text = tk.StringVar()  # 用于绑定输入框内容

        self.create_ui()  # 创建界面

    def create_ui(self):
        # 创建输入框区域
        input_frame = tk.Frame(self.root, height=50, bd=2, relief=tk.RIDGE)
        input_frame.pack(pady=10, fill="x")

        # 输入框
        input_field = tk.Entry(input_frame, font=('Arial', 24), textvariable=self.input_text, justify='right')
        input_field.pack(fill='both', ipady=10)

        # 按钮区域
        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        # 按钮布局
        buttons = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", ".", "=", "+", "Exit"]
        ]

        # 创建按钮并绑定事件
        for row in buttons:
            row_frame = tk.Frame(btns_frame)
            row_frame.pack(expand=True, fill='both')
            for btn in row:
                b = tk.Button(row_frame, text=btn, font=('Arial', 18), height=2, width=6,
                              command=lambda x=btn: self.on_button_click(x))  # 按钮点击事件
                b.pack(side='left', expand=True, fill='both')

    def on_button_click(self, char):
        # 清空输入
        if char == "C":
            self.expression = ""
            self.input_text.set("")
        # 计算表达式
        elif char == "=":
            try:
                result = str(round(eval(self.expression), 4))  # 计算并四舍五入到4位小数
                self.input_text.set(result)
                self.expression = result  # 结果作为下一次的表达式
            except Exception as e:
                messagebox.showerror("错误", "无效的表达式")  # 错误提示
                self.expression = ""
                self.input_text.set("")
        # 退出程序
        elif char == "Exit":
            self.root.quit()
        # 其他按钮（数字、运算符等）追加到表达式
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()  # 创建主窗口
    app = Calculator(root)  # 创建计算器实例
    root.mainloop()  # 进入主循环
