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
