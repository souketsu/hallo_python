from simpleeval import simple_eval  # 需先 pip install simpleeval
import math

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
            # 使用 simple_eval 安全计算表达式
            result = simple_eval(expr, functions=math.__dict__)
            history.append(f"{expr} = {result}")
            print("✅ 结果：", result)
            print("📜 输入 'history' 查看历史，输入 'exit' 退出程序\n")
        except Exception as e:
            print("❌ 错误的表达式，请重新输入。")
            print("提示：支持 + - * / 和括号")

if __name__ == "__main__":
    calculator()
