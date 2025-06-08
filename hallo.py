# 输出字符串"你好，世界"
print("你好，世界")
# 列出Python的常见数据类型
print("常见的数据类型有：")
print("1. int（整数）")
print("2. float（浮点数）")
print("3. str（字符串）")
print("4. bool（布尔值）")
print("5. list（列表）")
print("6. tuple（元组）")
print("7. dict（字典）")
print("8. set（集合）")
print("9. NoneType（空类型）")
# 变量的定义与使用示例
a = 10            # int
b = 3.14          # float
c = "Hello"       # str
d = True          # bool
e = [1, 2, 3]     # list
f = (4, 5, 6)     # tuple
g = {"name": "Tom", "age": 20}  # dict
h = {7, 8, 9}     # set
i = None          # NoneType

print("变量a的值为：", a)
print("变量b的值为：", b)
print("变量c的值为：", c)
print("变量d的值为：", d)
print("变量e的值为：", e)
print("变量f的值为：", f)
print("变量g的值为：", g)
print("变量h的值为：", h)
print("变量i的值为：", i)
# 基本运算示例
x = 8
y = 3

print("x + y =", x + y)      # 加法
print("x - y =", x - y)      # 减法
print("x * y =", x * y)      # 乘法
print("x / y =", x / y)      # 除法
print("x // y =", x // y)    # 整除
print("x % y =", x % y)      # 取余
print("x ** y =", x ** y)    # 幂运算
# 输入输出示例
user_input = input("请输入你的名字：")
print("你好，" + user_input + "！欢迎学习Python。")
# 条件语句示例
score = int(input("请输入你的分数："))
if score >= 90:
    print("成绩优秀")
elif score >= 60:
    print("成绩及格")
else:
    print("成绩不及格")
    # 循环语句示例
    print("for循环输出1到5：")
    for i in range(1, 6):
        print(i)

    print("while循环输出1到5：")
    j = 1
    while j <= 5:
        print(j)
        j += 1
        # 函数定义与调用示例
        def greet(name):
            print("你好，" + name + "！这是一个函数示例。")

        greet("小明")

        def add(x, y):
            return x + y

        result = add(5, 7)
        print("5 + 7 =", result)
        # 类与对象示例
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def say_hello(self):
                print("大家好，我是" + self.name + "，今年" + str(self.age) + "岁。")

        person1 = Person("小红", 18)
        person1.say_hello()