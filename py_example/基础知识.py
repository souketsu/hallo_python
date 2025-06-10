# 1. 变量与数据类型
name = "Alice"      # 字符串
age = 18            # 整数
height = 1.65       # 浮点数
is_student = True   # 布尔值

# 2. 类型转换
age_str = str(age)          # 整数转字符串
height_int = int(height)    # 浮点数转整数
num = float("3.14")         # 字符串转浮点数

# 3. 字符串操作
s = "Hello, Python!"
print(s.lower())            # 转小写
print(s.upper())            # 转大写
print(s.replace("Python", "World"))  # 替换
print(s[0:5])               # 切片，取前5个字符
print(len(s))               # 字符串长度

# 4. 基本输入输出
print("Hello, Python!")  # 输出
user_input = input("请输入你的名字：")  # 输入

# 5. 条件判断
if age >= 18:
    print("你已成年")
elif age >= 6:
    print("你是学生")
else:
    print("你未成年")

# 6. 循环
for i in range(3):
    print("循环次数：", i)

n = 0
while n < 3:
    print("while循环：", n)
    n += 1

# 7. 列表、元组、字典、集合
lst = [1, 2, 3]                # 列表
lst.append(4)                  # 添加元素
print(lst[1:3])                # 列表切片
tup = (4, 5, 6)                # 元组
dct = {"name": "Alice", "age": 18}  # 字典
print(dct["name"])             # 取值
st = {7, 8, 9}                 # 集合
st.add(10)                     # 添加元素

# 8. 推导式
squares = [x**2 for x in range(5)]  # 列表推导式
even_set = {x for x in range(10) if x % 2 == 0}  # 集合推导式
name_map = {x: chr(65 + x) for x in range(3)}    # 字典推导式

# 9. 函数定义与调用
def add(a, b):
    return a + b

print("3 + 5 =", add(3, 5))

# 10. 匿名函数和内置函数
double = lambda x: x * 2
print(list(map(double, [1, 2, 3])))  # [2, 4, 6]
print(list(filter(lambda x: x > 1, [1, 2, 3])))  # [2, 3]
print(sum([1, 2, 3]))  # 求和

# 11. 文件操作
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello, file!")

with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 12. 模块与导入
import math
print("平方根：", math.sqrt(16))

# 13. 异常处理
try:
    x = 1 / 0
except ZeroDivisionError:
    print("除数不能为0")
finally:
    print("无论如何都会执行")

# 14. 类与对象
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"你好，我是{self.name}，今年{self.age}岁。")

p = Person("小明", 20)
p.say_hello()

# 15. 常用标准库
import random
print(random.randint(1, 10))  # 随机整数

import datetime
print(datetime.datetime.now())  # 当前时间

# 16. 注释
# 这是单行注释
"""
这是多行注释
"""
