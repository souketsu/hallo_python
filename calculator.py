import math
'''
a = input("输入第一个数字") # 输入的第一个数
op = input("输入运算符 (+, -, *, /)") # 输入的运算符
b = input("输入第二个数字") # 输入的第二个数

def calculate(a, b, op):
    a = float(a)  # 将输入的字符串转换为浮点数
    b = float(b)  # 将输入的字符串转换为浮点数
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "除数不能为零"
        return a / b
    else:
        return "无效的运算符"

a = input("输入第一个数字：")
while True:
    op = input("输入运算符 (+, -, *, /)：")
    b = input("输入第二个数字（输入q退出）：")
    if b.lower() == "q":
        print("已退出计算器。")
        break
    result = calculate(a, b, op)
    print("结果是：", result)
    a = result  # 将上一次结果赋值给a

'''

history = []
def calculator():
   print("📟欢迎使用计算器！")
   print("🔢 请输入数学表达式，例如：3 + 4 * 2")
   print("📜 输入 'history' 查看历史，输入 'exit' 退出程序\n")

   while True:
       expr = input("请输入表达式：")
       if expr.lower() == "exit":
           print("已退出计算器。")
           break
       elif expr.lower() == "history":
           print("\n🕘 历史记录：")
           if not history:
               print("（暂无历史记录）")
           else:
               for i, item in enumerate(history, 1):
                   print(f"{i}. {item}")
           continue

       try:
           # 用 eval 计算表达式（注意安全，只用于练习）
           result = eval(expr, {"__builtins__": None}, math.__dict__)
           history.append(f"{expr} = {result}")
           print("✅ 结果：", result)
           print("📜 输入 'history' 查看历史，输入 'exit' 退出程序\n")
       except Exception as e:
           print("❌ 错误的表达式，请重新输入。")
           print("提示：支持 + - * / 和括号")

if __name__ == "__main__":
    calculator()
