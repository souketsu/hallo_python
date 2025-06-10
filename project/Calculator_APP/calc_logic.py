import math

class CalculatorEngine:
    def __init__(self, mode='deg'):
        self.mode = mode  # 'deg' 表示角度模式，'rad' 表示弧度模式

    def set_mode(self, mode):
        # 设置角度/弧度模式
        self.mode = mode

    def evaluate(self, expr: str):
        # 计算表达式，支持科学函数和常用运算
        try:
            expr = expr.replace("^", "**")  # 支持 ^ 为幂运算
            safe_dict = {
                'sqrt': math.sqrt,
                'log': math.log10,
                'ln': math.log,
                'pi': math.pi,
                'e': math.e,
                'pow': pow,
                'abs': abs
            }

            # 根据模式选择三角函数的实现
            if self.mode == 'deg':
                safe_dict.update({
                    'sin': lambda x: math.sin(math.radians(x)),
                    'cos': lambda x: math.cos(math.radians(x)),
                    'tan': lambda x: math.tan(math.radians(x)),
                })
            else:
                safe_dict.update({
                    'sin': math.sin,
                    'cos': math.cos,
                    'tan': math.tan,
                })

            result = eval(expr, {"__builtins__": {}}, safe_dict)
            return round(result, 10)
        except Exception:
            return None
