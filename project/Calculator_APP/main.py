import tkinter as tk  # 导入 Tkinter 图形界面库
from tkinter import messagebox, filedialog  # 导入消息框和文件对话框
from calc_logic import CalculatorEngine     # 导入计算核心模块
from history_logger import HistoryLogger    # 导入历史记录管理模块

class CalculatorApp:
    def __init__(self, root):
        # 初始化主窗口和变量
        self.root = root
        self.root.title("科学计算器")
        self.root.geometry("500x600")
        self.expression = ""      # 当前输入的表达式
        self.mode = "deg"         # 角度/弧度模式

        self.calc_engine = CalculatorEngine()  # 计算核心实例
        self.logger = HistoryLogger()          # 历史记录实例

        self.input_text = tk.StringVar()       # 输入框内容变量
        self.create_widgets()                  # 创建界面控件

    def create_widgets(self):
        # 创建输入框
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        self.input_entry = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 20), bd=5, relief=tk.RIDGE, width=30)
        self.input_entry.grid(row=0, column=0)
        self.input_entry.focus()
        self.input_entry.bind('<Return>', lambda event: self.on_button_click('='))  # 回车键绑定等号

        # 创建基础按钮区
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ['7', '8', '9', '/', 'sqrt('],
            ['4', '5', '6', '*', '^'],
            ['1', '2', '3', '-', '('],
            ['0', '.', '=', '+', ')'],
            ['⌫', 'C', '保存', '切换模式']
        ]

        # 动态生成基础按钮
        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(pady=2)
            for char in row:
                tk.Button(row_frame, text=char, font=('Arial', 14), width=7, height=2,
                          command=lambda c=char: self.on_button_click(c)).pack(side='left', padx=2)

        # 科学功能按钮区（可隐藏/显示）
        self.sci_frame = tk.Frame(button_frame)
        self.sci_frame.pack(pady=5)
        self.sci_buttons = []
        extra_buttons = ['sin(', 'cos(', 'tan(', 'log(', 'ln(', 'sqrt(', 'pi', 'e', '切换角度']
        for char in extra_buttons:
            btn = tk.Button(self.sci_frame, text=char, font=('Arial', 12), width=7, height=1,
                            command=lambda c=char: self.on_button_click(c))
            btn.pack(side='left', padx=2)
            self.sci_buttons.append(btn)

        # 历史记录显示区
        self.history_text = tk.Text(self.root, height=10, font=('Arial', 10), wrap='word')
        self.history_text.pack(fill='both', padx=10, pady=5)

        # 历史记录滚动条
        scrollbar = tk.Scrollbar(self.history_text, command=self.history_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.history_text.config(yscrollcommand=scrollbar.set)

    def on_button_click(self, char):
        # 按钮点击事件处理
        if char == '=':
            # 计算表达式
            result = self.calc_engine.evaluate(self.expression)
            if result is not None:
                full_expr = f"{self.expression} = {result}"
                self.input_text.set(str(result))
                self.logger.add(full_expr)
                self.history_text.insert('end', full_expr + '\n')
            else:
                messagebox.showerror("错误", "表达式无效")
        elif char == '⌫':
            # 删除最后一个字符
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == 'C':
            # 清空输入
            self.expression = ""
            self.input_text.set("")
        elif char == '保存':
            # 保存历史记录
            self.logger.save_to_txt()
            self.logger.save_to_csv()
            messagebox.showinfo("保存成功", "历史记录已保存为 TXT 和 CSV")
        elif char == '切换模式':
            # 显示/隐藏科学按钮区
            if self.sci_frame.winfo_ismapped():
                self.sci_frame.pack_forget()
            else:
                self.sci_frame.pack(pady=5)
            # 可选：切换背景色
            current = self.root.cget('bg')
            new = 'lightgrey' if current == 'SystemButtonFace' else 'SystemButtonFace'
            self.root.config(bg=new)
        elif char == "切换角度":
            # 切换角度/弧度模式
            self.mode = "rad" if self.mode == "deg" else "deg"
            self.calc_engine.set_mode(self.mode)
            messagebox.showinfo("角度模式切换", f"当前为：{'弧度' if self.mode == 'rad' else '角度'} 模式")
        elif char in ['sin(', 'cos(', 'tan(', 'log(', 'ln(', 'sqrt(']:
            # 输入科学函数
            self.expression += char
            self.input_text.set(self.expression)
        elif char in ['pi', 'e']:
            # 输入常数
            self.expression += char
            self.input_text.set(self.expression)
        else:
            # 其他字符直接追加
            self.expression += char
            self.input_text.set(self.expression)

if __name__ == '__main__':
    # 程序入口，启动主窗口
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
